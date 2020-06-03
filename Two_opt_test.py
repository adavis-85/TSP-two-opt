
# coding: utf-8

# In[ ]:


import numpy as np
import copy as cp
from time import perf_counter
import random

test=np.inf

a=np.random.rand(300,300)

for i in range(0,300):
    a[i,i]=np.inf

A=cp.deepcopy(a)
nv=[]
mn=[]
visited_at=[]
tv=[]


f,g=a.shape
bigA=cp.deepcopy(a)

cost=reduction_matrix_first(a)

node_values=[]
matrices=np.zeros((g-1,g,g))
A=cp.deepcopy(a)
cost_spot=0
for i in range(1,g):
    A=cp.deepcopy(a)
    A[:,i]=np.inf
    A[0]=np.inf
    cost_spot=a[0][i]
    A[i][0]=np.inf
    c=reduction_matrix_first(A)
    node_values.append(c+cost+cost_spot)
    matrices[i-1]=A

og_nodes=cp.deepcopy(node_values)    
og_nodes
visited_test=[]
visited_test.append(0)


visited_at.append(cp.deepcopy(visited_test))

mn.append(matrices)
nv.append(node_values)
node_values

insertion_for_test_visited=[]

insertion_for_test_visited=[None]*(g-len(visited_at))

for i in range(0,len(matrices)):
        inst=[]
        inst.append(0)
        for k in range(1,g):
            if all(matrices[i][:,k]==np.inf):
                inst.append(k)
        insertion_for_test_visited[i]=inst
        
tv.append(insertion_for_test_visited)

spot=np.argmin(nv[0])

visited_test.append(tv[0][spot].pop())

matrix_to_submit=cp.deepcopy(matrices[spot])

start=np.min(nv[0])

##Finding a first optimal path by branch and bound.
n=path_test(matrix_to_submit,start,visited_test,nv,mn,tv)

if len(n[2])<g:
    while len(n[2])<g:
        n=path_test((n[0]),(n[1]),(n[2]),(n[3]),(n[4]),(n[5]))
        
bigi=cp.deepcopy(n[2])     

##The cost of the path.
34.60819608942132

end=perf_counter()

execution_time=end-START

##The run-time to find the first optimal path.
execution_time

310.0671529639999

##Running the two opt test for 300 nodes.
lete_see=whole_thing(bigi,bigA)

##Cost of a feasible optimal path.  
30.920762082527897

##Runtime of the two opt test on 300 nodes.
383.8058852439999

