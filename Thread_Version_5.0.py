import time
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from itertools import permutations
from collections import deque
import numpy as np

global que

print("------------------------------------------------------------------------")
print("                    Job Tasks Optimization Program:                     ")
print("------------------------------------------------------------------------")
print("\n")
print("------------------------------------------------------------------------")
print("|          Now this Program can Optimize 10 number of Jobs.             |")
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
#newlist = map(str.upper, oldlist)
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

def fun1(permList,permString, result):
    for perm, stri in zip(permList, permString):
        #print("thread 1")#stri,"*" *5 ,perm)
        x=[]
        jb = JobTask(*perm)
        r = jb.opt_function()
        x.append(stri)
        #x.extend(perm)
        x.append(r)
        result.append(x)
        del jb
        
    return None


if __name__ == "__main__":
    s = time.time()
    permList = list(permutations(Data.values()))
    permString = list(permutations(Data.keys()))
    three_split_List = np.array_split(permList, 4)
    three_split_String = np.array_split(permString, 4)
    result1 = []
    result2 = []
    result3 = []
    result4 = []
    x = threading.Thread(target=fun1, args=(tuple(three_split_List[0].tolist()),tuple(three_split_String[0].tolist()), result1))
    y = threading.Thread(target=fun1, args=(tuple(three_split_List[1].tolist()),tuple(three_split_String[1].tolist()), result2))
    z = threading.Thread(target=fun1, args=(tuple(three_split_List[2].tolist()),tuple(three_split_String[2].tolist()), result3))
    w = threading.Thread(target=fun1, args=(tuple(three_split_List[3].tolist()),tuple(three_split_String[3].tolist()), result4))
    x.start()
    y.start()
    z.start()
    w.start()
    #Joined the threads
   
    #
    
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
print("-----------------------------------------------------------------------")
print("Time Taken tO Execute :")
print(e-s, "Sec")

pd.set_option("display.max_columns", None)
x.join()
y.join()
z.join()
w.join()

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
#DF.to_csv("myFile.csv")

n= input("Enter any key to exit:")