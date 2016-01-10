# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 11:29:03 2016

@author: Bram
"""

import pandas as pan
import codecs
import numpy as np
import os

#Find computer user
user=os.getlogin()

#Fine last session version
fileList=os.listdir("C:/Users/%s/Desktop/QuestionHistCrit/saves" %user)
fileList=sorted(fileList)
lastFile=fileList[-1]
numberFile=[int(s) for s in lastFile.split("_") if s.isdigit()]
numberFile=numberFile[0]

#Open lijst met foute stellingen
f = codecs.open ('C:/Users/%s/Desktop/QuestionHistCrit/vragenlijstFout.txt' %user,'r',"utf-8")

#Omzetting in array
q= pan.DataFrame(columns=['Question','Answer','explanationifFalse','AnswerShort'])
#line1=f.readline()
#f.readline()
#f.readline()
#line2=f.readline()
#f.readline()
#line3=f.readline()
#f.readline()
#f.readline()
#f.readline()
#data={'Question':[line1],'Answer':[line2],'explanationifFalse':[line3]}
#temp= pan.DataFrame(data,columns=['Question','Answer','explanationifFalse'])
#q=q.append(temp)



for x in range(0, 62):
    line1=f.readline()    
    f.readline()
    f.readline()
    line2=f.readline()
    f.readline()
    line3=f.readline()
    f.readline()
    f.readline()
    f.readline()
    data={'Question':[line1],'Answer':[line2],'explanationifFalse':[line3],'AnswerShort':['f']}
    temp= pan.DataFrame(data,columns=['Question','Answer','explanationifFalse','AnswerShort'])
    q=q.append(temp)
  
#Open lijst met juiste stelling in UTF-8 encoding
f = codecs.open ('C:/Users/%s/Desktop/QuestionHistCrit/vragenlijstJuist.txt' %user,'r',"utf-8")

for x in range(0, 93):
    line1=f.readline()    
    f.readline()
    f.readline()
    data={'Question':[line1],'Answer':['N/A'],'explanationifFalse':['N/A'],'AnswerShort':['t']}
    temp= pan.DataFrame(data,columns=['Question','Answer','explanationifFalse','AnswerShort'])
    q=q.append(temp)
    
f.close() 
    
#Re-index from dataframe
q.index=range(len(q))
    

#Initialising Main loop
counter=1;
score=0;
wrongList=pan.DataFrame(columns=['Question','Answer','explanationifFalse','AnswerShort']);
#Main loop

mode=input("Vorige sessie laden? (y/n):  ")
N=int(input("Hoeveel vragen ?: "))

if mode=="y":
    q=pan.read_csv("C:/Users/%s/Desktop/QuestionHistCrit/saves/session_%d_.csv" %(user,numberFile) ,encoding="utf-8")
    del q["Unnamed: 0"]    
while(counter<=N):
    randNum=np.random.randint(0,len(q.index))
    print(q.iloc[randNum,0])
    ans= input(" Answer (t/f): ")
    
    if not ans =='f' or ans =='t':
        while not (ans =='f' or ans =='t'):
            ans= input(" Answer (t/f): ")
            
    if ans==q.iloc[randNum,3]:
        score+=1;
        q=q.drop(randNum)
        q.index=range(len(q))       #reindex question 
        print("Right! :D")
        
    else:
        wrongList=wrongList.append(q.iloc[randNum,0:4])
        print("")
        print("")
        print("Wrong :(")
        print(q.iloc[randNum,1])
        print(q.iloc[randNum,2])
        input("Press Enter to continue...")        
        
    counter +=1;

print("")
print("")
print("Je score is %d / %d" % (score,N) )


#Alle foute samenvoegen bij de niet-gevraagde
numberFile +=1
q.to_csv("C:/Users/%s/Desktop/QuestionHistCrit/saves/session_%d_.csv" %(user,numberFile),encoding="utf-8")


