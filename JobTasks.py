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
max_size = 8
que = deque(maxlen= max_size)

class JobTask():
    "This is Job Task Management class"
    que.clear()
    count = 0
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    
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
    
    def opt_function(self):

        que.extend(self.a)
    
        '''for j in self.b:
            if j not in list(que):
                que.put(j)
            else:
                pass'''
        self.cal(self.b)
        self.cal(self.c)
        return self.cal(self.d)#, print(self.count)
    
    

s = time.time()
A = [2,3,4,5]
B = [8,7,2,3]
C = [4,5,6,7]
D = [8,9,2,6]

jb = JobTask([8, 9, 2, 6], [4, 5, 6, 7], [8, 7, 2, 3], [2, 3, 4, 5])

print(jb.opt_function())
print(jb.a, jb.b, jb.c, jb.d, list(que))
e = time.time()
#print(dir(jb))
print(e-s)
del jb

'''permList = permutations([A,B,C,D])

# print all permutations 
for perm in list(permList):
    #print(perm)
    jb = JobTask(perm[0], perm[1], perm[2], perm[3])
    result = jb.opt_function()
    if result == 2:
        print(perm)
    else:
        pass
    del jb'''
        
