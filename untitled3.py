import multiprocessing as mp
from itertools import permutations
from collections import deque

#Example of multiprocessing
'''
def func(i):

    return i ** i

def sum_up_to(number):
    return sum(range(1, number + 1))




   # pool = multiprocessing.Pool(processes=2)
    #all_processes = [pool.apply_async(func, (i, )) for i in range(1, 5)]

    #for process in all_processes:
        #val = process.get()
        #print(val)
        
    
    a_pool = multiprocessing.Pool()
    #Create pool object


    result = a_pool.map(sum_up_to, range(10))
    #Run `sum_up_to` 10 times simultaneously

    print(result)


print("Cpu Count :",mp.cpu_count())

import numpy as np
from time import time

# Prepare data
np.random.RandomState(100)
arr = np.random.randint(0, 10, size=[200000, 5])
data = arr.tolist()
print(data[:5])


def howmany_within_range(row, minimum, maximum):
    """Returns how many numbers lie within `maximum` and `minimum` in a given `row`"""
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count

results = []
for row in data:
    results.append(howmany_within_range(row, minimum=4, maximum=8))

print(results[:10])

if __name__ == "__main__":
# Step 1: Init multiprocessing.Pool()
    pool = mp.Pool(mp.cpu_count())

# Step 2: `pool.apply` the `howmany_within_range()`
    results = [pool.apply(howmany_within_range, args=(row, 4, 8)) for row in data]

# Step 3: Don't forget to close
    pool.close()    

    print(results[:10])
    '''
    
    
Data = {'A': [2, 3, 4, 5, 6, 7],
 'B': [8, 7, 2, 3, 4, 9],
 'C': [4, 5, 6, 7, 3, 8],
 'D': [8, 9, 2, 6, 1, 5],
 'E': [5, 2, 6, 3, 4, 8],
 'F': [6, 3, 4, 8, 2, 7],
 'G': [9, 5, 1, 2, 4, 3, 6, 8, 2]}

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
        #for j in self.args[1:len(self.args)]:
            #self.cal(j)
        
        return pool.map(self.count,self.args[1:len(self.args)])

if __name__ == "__main__":
    #s = time.time()
    permList = permutations(Data.values())
    permString = permutations(Data.keys())
    result = []
    pool = mp.Pool(mp.cpu_count()-1)
    for perm, stri in zip(list(permList), list(permString)):

        x=[]
        jb = JobTask(*perm)
        r = jb.opt_function()
        x.append(stri)
        x.append(r)
        result.append(x)
        del jb