
# coding: utf-8

# In[ ]:


def path_test(mate,val,visited,N,M,T):
    
    d,e=mate.shape
    ranges=list(range(0,d))
    
    matrix_to_test=np.zeros((e,e))
    
    node_val=[]
    
    ##Checking if nodes have been visited out of the mandatory length that the path
    ##will have to be.  
    j=np.isin(ranges,visited)

    cost_spot=0
    
    ##Matrices for the path.  Each matrix needs to be saved for the purpose of using to
    ##search on.  
    matrices=[None]*(e-len(visited))
    
    l=0
    
    for i in range(0,e):
        if not j[i]:
            ##The last node and the second to last nodes spots in the original matrix are also
            ##added to the cost each time for the node value chosen.
            cost_spot=a[visited[-2]][visited[-1]]
            ##A copy of the matrix is made so that it is not changed.  It is saved.  
            A=cp.deepcopy(mate)
            ##The spot of the matrix corresponding to the visited nodes is represented.
            ##A[visited]=np.inf
            A[visited]=np.inf
            A[:,i]=np.inf
            ##Cost spot is changed
            A[visited[-1]][visited[-2]]=np.inf
            c=reduction_matrix_first(A)
            
            
            ##The value of the path specific node is saved
            node_val.append(c+val+cost_spot)
            ##The searched matrix is saved into the grouping for the path search.
            matrices[l]=A
            l+=1
            
    value_check=np.inf
    nee=cp.deepcopy(visited)
    M.append(matrices)
    N.append(node_val)
    
    
    insertion_for_test_visited=[None]*(e-len(visited))
    
    for i in range(0,len(matrices)):
        inst=[]
        
        for m in range(0,len(nee)):
            inst.append(nee[m])
            
        j=np.isin(ranges,nee)
        
        for k in range(0,e):
            if not j[k]:
                dee=cp.deepcopy(matrices[i][:,k])
                if all(dee==np.inf):
                    inst.append(k)
                    
        insertion_for_test_visited[i]=cp.deepcopy(inst)
        
    T.append(insertion_for_test_visited)
                
    for i in range(0,len(node_val)):
        if value_check>node_val[i]:
            value_check=cp.deepcopy(node_val[i])
            matrix_to_test=cp.deepcopy(matrices[i])
        
    blocked_row_inf=[]
    
    for i in range(0,len(j)):
        if not j[i]:
            d=cp.deepcopy(matrix_to_test[:,i])
            if np.all(d==np.inf):
                blocked_row_inf.append(i)
                visited.append(i)
        
    matrix_to_test[blocked_row_inf]=np.inf
    
   
    if len(visited)==e:
        value_check+=a[visited[-1]][visited[0]]
        visited.append(visited[0])
        
        
    return (matrix_to_test,value_check,visited,N,M,T)

def k_opt_cost(new_path,matr):
    
    
    ##Find the cost of the first matrix reduction
    c=reduction_matrix_first(matr)
    
    neat=cp.deepcopy(matr)
    
    total_cost=c
    
    for i in range(1,len(new_path)):
        
    
        added_cost=matr[new_path[i-1]][new_path[i]]
        neat[new_path[i]][new_path[i-1]]=np.inf
        
        
        
        neat[:,new_path[i]]=np.inf
        neat[new_path[i-1]]=np.inf
        
        ##The cost of the matrix reduction for each visited node.
        d=reduction_matrix_first(neat)
        
        
        
        total_cost+=d+added_cost
        
        
        
    return total_cost


def two_opt(eye,kay,path):
    
    ##Two opt implementation on the path.  
    first=path[:eye]
        
    second=path[eye:kay]
    
    second=second[::-1]
    
    third=path[kay:]
   
    inc=first+second+third

    return inc

    
def whole_thing(old_route,start_matrix):
    
    a=cp.deepcopy(start_matrix)
    
    START=perf_counter()
    
    ##Cost of the first path
    incumbent=k_opt_cost(old_route,a)
    
    new_route=old_route
    
    inc=incumbent
    
    BEGIN=perf_counter()
    
    
    
    for i in range(1,len(old_route)-2):
        
        
        
            for k in range(i+2,len(old_route)):

                a=cp.deepcopy(start_matrix)
                test_route=two_opt(i,k,new_route)

                test_cost=k_opt_cost(test_route,a)
        ##If the two opt operation on the path is decreasing then the function keeps 
        ##going.  Or else it goes to the next point.
                if (test_cost-inc)<=0:

                    inc=cp.deepcopy(test_cost)
                    new_route=cp.deepcopy(test_route)
                    end=perf_counter() 
                else:
                    break
            
            
    END=perf_counter()  
    TIME=END-BEGIN
    
    return inc,new_route,TIME



