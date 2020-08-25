# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 12:58:23 2020

@author: 20TE147
"""
import time
from collections import deque
from itertools import permutations


'''for j in L2:
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
            pass'''

global que

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
'''
print("Enter Tasks for Job A: ")
A = [int(input()) for _ in range(n)]
print("Enter Tasks for Job B: ")
B = [int(input()) for _ in range(n)]
print("Enter Tasks for Job C: ")
C = [int(input()) for _ in range(n)]
print("Enter Tasks for Job D: ")
D = [int(input()) for _ in range(n)]
print("Enter Tasks for Job E: ")
E = [int(input()) for _ in range(n)]
print("Enter Tasks for Job F: ")
F = [int(input()) for _ in range(n)]
'''
def Inp(n):
    
    b = []
    while n > 0:
        
        try:
            b.append(int(input()))
            n -=1
        
        except ValueError:
            print("Sorry, I didn't understand that.")
            print("try one more time")
            #better try again... Return to the start of the loop
            continue
    
    return b
'''
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
'''
A = [2,3,4,5,6,7]
B = [8,7,2,3,4,9]
C = [4,5,6,7,3,8]
D = [8,9,2,6,1,5]
E = [5,2,6,3,4,8]
F = [6,3,4,8,2,7]
print("------------------------------------------------------------------------")

print("Job A Taks {}".format(A))
print("Job B Taks {}".format(B))
print("Job C Taks {}".format(C))
print("Job D Taks {}".format(D))
print("Job E Taks {}".format(E))
print("Job F Taks {}".format(F))

print("------------------------------------------------------------------------")

max_size = int(input("Enter Feeder size (Queue Size) "))
que = deque(maxlen= max_size)


class JobTask():
    "This is Job Task Management class"
    que.clear()
    count = 0
    def __init__(self,*args):
        self.args = args
    
    def cal(self,z):
        for j in z:
            if j not in list(que):
                if len(que) < max_size:
                    que.append(j)
                    self.count +=1
                #print(j)
                #print('Queue',list(que))
                else:
                    que.popleft()
                    que.append(j)
                    self.count +=2
                #print(j)
                #print('Queue',list(que))
            else:
                pass
        
        return self.count
    
    def opt_function(self, *args):
        que.extend(self.args[0])
        for j in self.args[1:len(self.args)]:
            self.cal(j)
        
        return self.count
         
    


#A = [2,3,4,5]
#B = [8,7,2,3]
#C = [4,5,6,7]
#D = [8,9,2,6]
A = [2,3,4,5,6,7]
B = [8,7,2,3,4,9]
C = [4,5,6,7,3,8]
D = [8,9,2,6,1,5]
E = [5,2,6,3,4,8]
F = [6,3,4,8,2,7]





'''jb = JobTask([8, 9, 2, 6], [4, 5, 6, 7], [8, 7, 2, 3], [2, 3, 4, 5])

print(jb.opt_function())
print(jb.a, jb.b, jb.c, jb.d, list(que))
e = time.time()
#print(dir(jb))
print(e-s)
del jb

'''
s = time.time()
permList = permutations([A,B,C,D,E,F])
permString = permutations("ABCDEF")

result = []
# print all permutations
for perm, stri in zip(list(permList), list(permString)):
    #print(perm)
    x=[]
    jb = JobTask(*perm)
    r = jb.opt_function()
    x.append(stri)
    x.extend(perm)
    x.append(r)
    result.append(x)
    #print("DeQueue", que)
    #print('Count of operations', result)
    #print(perm)
    #if result == 2:
    #   print(perm)
    #else:
    #   pass
    del jb

e = time.time()
print("-----------------------------------------------------------------------")
print("Time Taken tO Execute :")
print(e-s, "Sec")

import pandas as pd
pd.set_option("display.max_columns", None)


dataFrame = pd.DataFrame(result,)
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
print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
print("|                        Result LookUp                             |")
print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\")
print("Less then 10 Operations Results (Can or Can not be present)")
print(DF.sort_values(by=['Count_of_Operations']).head(10))
#dataFrame.to_csv("myFile.csv")
#install Auto py to Exe

#time.sleep(500)
#time.sleep(500)
n = input("Press Any key to exit: ")


#dataFrame.to_csv("myFileofJobTasksfile.csv")     
