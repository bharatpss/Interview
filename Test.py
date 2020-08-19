# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 16:41:13 2020

@author: 20TE147
"""
import time


s = time.time()
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
    que.queue.clear()
    count = 0
    for i in L1:
        que.put(i)
    
    for j in L2:
        if j not in list(que.queue):
            que.put(j)
        else:
            pass
    
    #print(list(que.queue))    
    for i in L3:
        if i not in list(que.queue):
            que.get()
            que.put(i)
            count +=2
        
        #print(i)
        else:
        #print(new)
            pass
    #print(list(que.queue))
    #print(count)

    for i in L4:
        if i not in list(que.queue):
            que.get()
            que.put(i)
            count +=2
        #print(i)
        else:
        #print(new)
            pass
    #print(list(que.queue))
    return(count)
        
        
#opt_function(A,B,C,D)
             
from itertools import permutations 
#import string
permList = permutations([A,B,C,D])
  
# print all permutations 
for perm in list(permList): 
    #print(perm)
    result = opt_function(perm[0], perm[1], perm[2], perm[3])
    if result == 2:
        print(perm)
    else:
        pass
             
#print(a_set.union(b_set))
#que.put(a_set.union(b_set))
#print(list(que.queue))
#new = a_set.union(b_set)
e = time.time()
print(e-s)
