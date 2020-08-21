# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 11:03:38 2020

@author: 20TE147
"""
import time
from collections import deque
from itertools import permutations
import pandas as pd
pd.set_option("display.max_columns", None)

print("------------------------------------------------------------------------")
print("                    Job Tasks Optimization Program:                     ")
print("------------------------------------------------------------------------")
print("Note:")
#print("1. If Entered numbers are like this : 2 5 9 f 5 2 6 g 5 6.\nThen program take [2, 5, 9, 5, 2, 6, 5, 6] as an inputs.")
'''
try:
    A = [int(i) for i in input("Enter number of elements : ").strip().split() if i.isdigit()]
except ValueError:
    print("That wasn't an integer :(")
'''

print("1. For Performing N number of jobs Program is Under Construction")
print("            ⚠ Content will be available soon ⚠               ")
print("------------------------------------------------------------------------")
print("|          As of Now this Program can Optimize 6 Jobs Only.            |")
print("|   Please enter one Task and hit enter to feed another task in Job:   |")
print("------------------------------------------------------------------------")

n = int(input("Enter count of tasks need to assign to job: "))

#A = [int(i) for i in input("Enter number of elements : ").strip().split() if i.isdigit()]
print("------Tasks need to be enter in Interger between (1-9)----")
#print("Enter Tasks for Job A: ")

def Inp(n):
    
    b = []
    while n > 0:
        
        try:
            b.append(int(input()))
            n -=1
        
        except ValueError:
            print("Sorry, I didn't understand that.")
            print("Enter correct serise at one time")
            #better try again... Return to the start of the loop
            continue
    
    return b


print("Enter Tasks for Job A: ")
#A = [int(input()) for _ in range(n)]
A = Inp(n)
print("Enter Tasks for Job B: ")
#B = [int(input()) for _ in range(n)]
B = Inp(n)
print("Enter Tasks for Job C: ")
#C = [int(input()) for _ in range(n)]
C = Inp(n)
print("Enter Tasks for Job D: ")
#D = [int(input()) for _ in range(n)]
D = Inp(n)
print("Enter Tasks for Job E: ")
E = Inp(n)
#E = [int(input()) for _ in range(n)]
print("Enter Tasks for Job F: ")
#F = [int(input()) for _ in range(n)]
F = Inp(n)

print("------------------------------------------------------------------------")

print("Job A Taks {}".format(A))
print("Job B Taks {}".format(B))
print("Job C Taks {}".format(C))
print("Job D Taks {}".format(D))
print("Job E Taks {}".format(E))
print("Job F Taks {}".format(F))

print("------------------------------------------------------------------------")
'''
max_size = int(input("Enter Feeder size (Queue Size) "))



que = deque(maxlen= max_size)

def opt_function(L1,L2,L3,L4,L5,L6):
    
    que.clear()
    count = 0
    #print('Queue',list(que))
    
    #for i in L1:
        #que.append(i)
    que.extend(L1)
    
    #print('Queue',list(que))
    
    for j in L2:
        if j not in list(que):
            if len(que) < max_size:
                que.append(j)
                count +=1
                #print(j)
                #print('Queue',list(que))
            else:
                que.popleft()
                que.append(j)
                count +=2
                #print(j)
                #print('Queue',list(que))
        else:
            pass
    
    #print('Queue',list(que))    
    #print(count)
    for k in L3:
        if k not in list(que):
            if len(que) < max_size:
                que.append(k)
                count +=1
                #print(k)
                #print('Queue',list(que))
            else:
                que.popleft()
                que.append(k)
                count +=2
                #print(k)
                #print('Queue',list(que))
        
        
        else:
            pass
    #print('Queue',list(que))
    #print(count)

    for l in L4:
        if l not in list(que):
            if len(que) < max_size:
                que.append(l)
                count +=1
                #print(l)
                #print('Queue',list(que))
            else:
                que.popleft()
                que.append(l)
                count +=2
                #print(l)
                #print('Queue',list(que))
        
        else:
    
            pass
        
    #print('Queue',list(que))
   # print(count)
    
    for m in L5:
        if m not in list(que):
            if len(que) < max_size:
                que.append(m)
                count +=1
                #print(m)
                #print('Queue',list(que))
            else:
                que.popleft()
                que.append(m)
                count +=2
                #print(m)
                #print('Queue',list(que))
        
        else:
            pass
        
    #print('Queue',list(que))
    #print(count)
    
    for n in L6:
        if n not in list(que):
            if len(que) < max_size:
                que.append(n)
                count +=1
                #print(n)
                #print('Queue',list(que))
            else:
                que.popleft()
                que.append(n)
                count +=2
                #print(n)
                #print('Queue',list(que))
    
        else:
        
            pass
    #print('Queue',list(que))
    print(count)
    return(count)

s = time.time()
#import string
permList = permutations([A,B,C,D,E,F])
permString = permutations("ABCDEF")
# print all permutations 
result = []
for perm, stri in zip(list(permList), list(permString)): 
    #print(perm)
    x=[]
    r = opt_function(perm[0], perm[1], perm[2], perm[3],perm[4],perm[5],)
    x.append(stri)
    x.extend(perm)
    x.append(r)
    result.append(x)
    
    #if r <= 5:
     #   print(perm)
      #  print(stri)
    #else:
     #   pass
    

e = time.time()
print(e-s)



dataFrame = pd.DataFrame(result)
#columns=['Permutations', "JobSeq1"	,"JobSeq2",	"JobSeq3",	"JobSeq4",	"JobSeq5",	"JobSeq6",	"Count of  Operations"]

DF = pd.DataFrame()

DF['Permutations'] = dataFrame[0]
DF['JobSeq1'] = dataFrame[1]
DF['JobSeq2'] = dataFrame[2]
DF['JobSeq3'] = dataFrame[3]
DF['JobSeq4'] = dataFrame[4]
DF['JobSeq5'] = dataFrame[5]
DF['JobSeq6'] = dataFrame[6]
DF['Count_of_Operations'] = dataFrame[7]

#print("Result in Table formate")
#print(DF.sort_values(by=['Count_of_Operations']))

print("Less then 10 Operations Results (Can or Can not be present)")
print(DF[DF["Count_of_Operations"] < 10].sort_values(by=['Count_of_Operations']).head(10))
#dataFrame.to_csv("myFile.csv")
#install Auto py to Exe

#time.sleep(500)
#time.sleep(500)
n = input("Press something to exit")

'''
