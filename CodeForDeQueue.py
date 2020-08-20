# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 15:14:48 2020

@author: 20TE147
"""

'''dq = deque(maxlen=8)
print('Queue',list(dq))
dq.extend([5, 2, 6, 3, 4, 8])
print('Queue',list(dq))
for j in [2, 3, 4, 5, 6, 7]:
    print(j)
    if j not in list(dq):
        print(j,"not in queue")
            
        if len(dq)<=8:
                dq.append(j)
                #count +=1
                print(j)
                print('Queue',list(dq))
        else:
                dq.popleft()
                dq.append(j)
                #count +=2
                print(j)
                print('Queue',list(dq))
    else:
          pass
print('Queue',list(dq))
print(len(dq))
print(list(dq))'''


from collections import deque
import time



A = [2,3,4,5,6,7]
B = [8,7,2,3,4,9]
C = [4,5,6,7,3,8]
D = [8,9,2,6,1,5]
E = [5,2,6,3,4,8]
F = [6,3,4,8,2,7]

s = time.time()
max_size = 10

#from collections import deque

que = deque(maxlen= max_size)



def opt_function(L1,L2,L3,L4,L5,L6):
    que.clear()
    count = 0
    print('Queue',list(que))
    
    #for i in L1:
        #que.append(i)
    que.extend(L1)
    
    print('Queue',list(que))
    print('count',count)
    for j in L2:
        if j not in list(que):
            if len(que) < max_size:
                que.append(j)
                count +=1
                print(j)
                print('Queue',list(que))
            else:
                que.popleft()
                que.append(j)
                count +=2
                print(j)
                print('Queue',list(que))
        else:
            pass
    
    print('Queue',list(que))    
    print('count',count)
    for k in L3:
        if k not in list(que):
            if len(que) < max_size:
                que.append(k)
                count +=1
                print(k)
                print('Queue',list(que))
            else:
                que.popleft()
                que.append(k)
                count +=2
                print(k)
                print('Queue',list(que))
        
        
        else:
            pass
    print('Queue',list(que))
    print('count',count)

    for l in L4:
        if l not in list(que):
            if len(que) < max_size:
                que.append(l)
                count +=1
                print(l)
                print('Queue',list(que))
            else:
                que.popleft()
                que.append(l)
                count +=2
                print(l)
                print('Queue',list(que))
        
        else:
    
            pass
        
    print('Queue',list(que))
    print('count',count)
    
    for m in L5:
        if m not in list(que):
            if len(que) < max_size:
                que.append(m)
                count +=1
                print(m)
                print('Queue',list(que))
            else:
                que.popleft()
                que.append(m)
                count +=2
                print(m)
                print('Queue',list(que))
        
        else:
            pass
        
    print('Queue',list(que))
    print('count',count)
    
    for n in L6:
        if n not in list(que):
            if len(que) < max_size:
                que.append(n)
                count +=1
                print(n)
                print('Queue',list(que))
            else:
                que.popleft()
                que.append(n)
                count +=2
                print(n)
                print('Queue',list(que))
    
        else:
        
            pass
    print('Queue',list(que))
    print('count',count)
    return(count)

opt_function([2, 3, 4, 5, 6, 7],	[8, 9, 2, 6, 1, 5],	[5, 2, 6, 3, 4, 8],	[4, 5, 6, 7, 3, 8],	[8, 7, 2, 3, 4, 9],	[6, 3, 4, 8, 2, 7]
)