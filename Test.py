# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 16:41:13 2020

@author: 20TE147
"""
import time



A = [2,3,4,5]
B = [8,7,2,3]
C = [4,5,6,7]
D = [8,9,2,6]

max_size = 8

import queue

que = queue.Queue(max_size)



a_set = set(A)
b_set = set(B)
c_set = set(C)

'''if len(a_set.intersection(b_set)) > 0: 
    print(a_set.intersection(b_set))   
else: 
    print("no common elements") 
'''

def opt_function(L1,L2,L3,L4):
    count = 0
    for i in L1:
        que.put(i)
    
    for j in L2:
        if j not in list(que.queue):
            que.put(j)
        else:
            pass
    
    print(list(que.queue))    
    for i in L3:
        if i not in list(que.queue):
            que.get()
            que.put(i)
            count +=2
        
        #print(i)
        else:
        #print(new)
            pass
    print(list(que.queue))
    print(count)

    for i in L4:
        if i not in list(que.queue):
            que.get()
            que.put(i)
            count +=2
        #print(i)
        else:
        #print(new)
            pass
    print(list(que.queue))
    print(count)
        
        
#opt_function(A,B,C,D)
             
from itertools import permutations 
import string
permList = permutations("ABCD")
  
# print all permutations 
for perm in list(permList): 
    print (perm[0])
    #opt_function(','.join(perm))
             
#print(a_set.union(b_set))
#que.put(a_set.union(b_set))
#print(list(que.queue))
#new = a_set.union(b_set)
print(type(A))

'''
for i in c_set:
    if i not in new:
        #que.put(i)
        new.add(i)
        #print(i)
    else:
        print(new)
        #pass
        '''       
        
#print(list(que.queue))

'''a = lambda x:x**2
print(a(5))'''

'''print('A', a_set)
print('B', b_set)
print(a_set.union(b_set))
print(a_set.intersection(b_set))
print(a_set - b_set)
print(b_set - a_set)
print(a_set ^ b_set)
print(b_set ^ a_set)
print(a_set.symmetric_difference(b_set))'''





























