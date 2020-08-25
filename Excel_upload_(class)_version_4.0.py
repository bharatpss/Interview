# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 15:38:12 2020

@author: 20TE147
"""


import time
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from itertools import permutations
from collections import deque

global que

print("------------------------------------------------------------------------")
print("                    Job Tasks Optimization Program:                     ")
print("------------------------------------------------------------------------")
print("\n")
print("------------------------------------------------------------------------")
print("|          Now this Program can Optimize N number of Jobs.             |")
print("|              Please Select the xls format file:                      |")
print("------------------------------------------------------------------------")
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

#print(pd.read_csv(file_path).head())
file = pd.ExcelFile(file_path )



# to read all sheets to a map
Data = {}
for sheet_name in file.sheet_names:
    Data[sheet_name] = file.parse(sheet_name, header=None, usecols=[0], index_col=False).iloc[:,0].to_list()

#print(file.parse('A', header=None, usecols=[0], index_col=False).iloc[:,0].to_list())


    

'''print(Data)
print(len(Data))
'''
for key,val in Data.items():
    print(key, "=>", len(val)) 
    
print("------------------------------------------------------------------------")
l =[]
for i in Data.values():
    l.extend(i)
    
print("Unique count of tasks", len(set(l)))
print("------------------------------------------------------------------------")

max_size = int(input("Enter Feeder size (Queue Size) :"))
que = deque(maxlen= max_size)
print("\n")






    
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
            
if __name__ == "__main__":
    s = time.time()
permList = permutations(Data.values())
permString = permutations(Data.keys())
result = []
for perm, stri in zip(list(permList), list(permString)):
    #print(stri,"*" *5 ,perm)
    x=[]
    jb = JobTask(*perm)
    r = jb.opt_function()
    x.append(stri)
    #x.extend(perm)
    x.append(r)
    result.append(x)
    del jb
    
    
e = time.time()
print("-----------------------------------------------------------------------")
print("Time Taken tO Execute :")
print(e-s, "Sec")

#import pandas as pd
pd.set_option("display.max_columns", None)


dataFrame = pd.DataFrame(result,)
DF = pd.DataFrame()

DF['Permutations'] = dataFrame[0]
DF['Count_of_Operations'] = dataFrame[1]

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

