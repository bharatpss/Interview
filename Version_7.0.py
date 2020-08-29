# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 11:55:37 2020

@author: 20TE147
"""
import time
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from itertools import permutations
from collections import deque
import numpy as np
global que
np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)
pd.set_option('display.max_colwidth',None)


print("------------------------------------------------------------------------")
print("                    Job Tasks Optimization Program:                     ")
print("------------------------------------------------------------------------")
print("\n")
print("------------------------------------------------------------------------")
print("|          Now this Program can Optimize 10 PCBs at a Time.             |")
print("|                Please Select the xls file format:                     |")
print("------------------------------------------------------------------------")

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(title = "Select file",filetypes = (("Excel files","*.xls*"),("all files","*.*")))

#print(pd.read_csv(file_path).head())
#file = pd.ExcelFile(file_path )
dataFrame = pd.read_excel(file_path, keep_default_na=False)

Data={}

for i in dataFrame.columns[3:-1]:
    Data[i] = list(dataFrame[dataFrame[i]==1]['Component_Desc'][:-1])
    
    
    

print("------------------------------------------------------------------------")
# key,val in Data.items():
 #   print(key, "=>", val) 
print("---------------------If Pcbs Having Same Components---------------------")
same_pcbs = []

for k, v in Data.items():
    print("-"*25,"****","-"*25)
    if list(Data.values()).count(v)>1:
        print(k, "PCBs have same components with size :", len(v))
        same_pcbs.append(k)
print("------------------------------------------------------------------------")
result = {}

for key,value in Data.items():
    if value not in result.values():
        result[key] = value
        
print("PCB Type", "=>", "Count of component")        
for key,val in result.items():
    print(key, "=>", len(val)) 
    
print("------------------------------------------------------------------------")
l =[]
#newlist = map(str.upper, oldlist)
for i in Data.values():
    l.extend(i)
    
print("Unique count of tasks", len(set(l)))
print("------------------------------------------------------------------------")


max_size = int(input("Enter Feeder size (Queue Size) :"))
que = deque(maxlen= max_size)


class JobTask():
    "This is Job Task Management class"
    que.clear()
    count = 0
    def __init__(self,*args):
        self.args = args
    
    def cal(self,z):
        # From previous funtion of O(n2)
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
        #complexsity O(n) depending on Argument length.
        for j in self.args[1:len(self.args)]:
            self.cal(j)
        
        return self.count


import threading

global result1, result2, result3, result4

def fun1(permList,permString, result, lock):
    for perm, stri in zip(permList, permString):
        lock.acquire()
        #print("thread 1")#stri,"*" *5 ,perm)
        x = []
        jb = JobTask(*perm)
        r = jb.opt_function()
        x.append(stri)
        #x.extend(perm)
        x.append(r)
        result.append(x)
        del jb
        lock.release()
    return result


if __name__ == "__main__":
    s = time.time()
    permList = list(permutations(result.values()))
    permString = list(permutations(result.keys()))
    three_split_List = np.array_split(permList, 4)
    three_split_String = np.array_split(permString, 4)
    lock = threading.Lock()
    result1 = []
    result2 = []
    result3 = []
    result4 = []
    x = threading.Thread(target=fun1, args=(tuple(three_split_List[0].tolist()),tuple(three_split_String[0].tolist()), result1, lock))
    y = threading.Thread(target=fun1, args=(tuple(three_split_List[1].tolist()),tuple(three_split_String[1].tolist()), result2, lock))
    z = threading.Thread(target=fun1, args=(tuple(three_split_List[2].tolist()),tuple(three_split_String[2].tolist()), result3, lock))
    w = threading.Thread(target=fun1, args=(tuple(three_split_List[3].tolist()),tuple(three_split_String[3].tolist()), result4, lock))
    x.start()
    y.start()
    z.start()
    w.start()
    #Joined the threads
    x.join()
    y.join()
    z.join()
    w.join()
   
    
    
    #Perallel Processing with O(n!) input to Time Complexity with O(n)
    '''for perm, stri in zip(permList, permString):
        #print(stri,"*" *5 ,perm)
        x=[]
        jb = JobTask(*perm)
        r = jb.opt_function()
        x.append(stri)
        #x.extend(perm)
        x.append(r)
        result.append(x)
        del jb'''
    
    
e = time.time()
print("------------------------------------------------------------------------")
print("Time Taken tO Execute :")
print(e-s, "Sec")
print("------------------------------------------------------------------------")
pd.set_option("display.max_columns", None)


dataFrame1 = pd.concat([pd.DataFrame(result1,),pd.DataFrame(result2,),pd.DataFrame(result3,),pd.DataFrame(result4,)])
#dataFrame2 = pd.DataFrame(result2,)
DF = pd.DataFrame()

DF['Permutations'] = dataFrame1[0]
DF['Count_of_Operations'] = dataFrame1[1]

#print("Result in Table formate")
#print(DF.sort_values(by=['Count_of_Operations']))
print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
print("|                        Result LookUp                             |")
print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\")
print("Less then 10 Operations Results (Can or Can not be present)")
print(DF.sort_values(by=['Count_of_Operations']).head(10))
print("------------------------------------------------------------------------")
print("Save File to your prefered location:")
print("------------------------------------------------------------------------")

if DF.shape[0] >= 100000:
    DF = DF.sort_values(by=['Count_of_Operations']).head(10000)
else:
    pass    
    
while True:
    try:
        savefile = filedialog.asksaveasfilename(title = "Save file",filetypes = (("Excel files","*.xls*"),("all files","*.*")))               
        DF.sort_values(by=['Count_of_Operations']).to_excel(savefile + ".xls", index=False, sheet_name="Results")         
        print("-----------------------------------------------------------------------")
        print("Completed saving.....")
        print("-----------------------------------------------------------------------")
        break
    except ValueError:
        print("-----------------------------------------------------------------------")
        print("Error. Please try again.")
        print("-----------------------------------------------------------------------")
    #showerror("Open correct Source File", "Failed to import file\n'%s'" % file)

              
#DF.to_csv("myFile.csv")

n= input("Enter any key to exit:")