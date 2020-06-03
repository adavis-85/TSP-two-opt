# TSP-two-opt

   One way to find a faster solution to the TSP problem is to use a two-opt algorithm.  The two-opt is a local search 
algorithm.  The basic idea to the procedure is to search for two sets of points on the route and arrange them so 
that they don't cross.  If the cost of this new path is less than the one before then the new path is kept.  The search isstopped after a swap that doesn't result in a decreased total cost.  
    ```
    for i in range(1,len(old_route)-2):
        
        for k in range(i+2,len(old_route)):

                a=cp.deepcopy(start_matrix)
                
                test_route=two_opt(i,k,new_route)

                test_cost=k_opt_cost(test_route,a)
        
                if (test_cost-inc)<=0:

                    inc=cp.deepcopy(test_cost)
                    new_route=cp.deepcopy(test_route)
                    end=perf_counter() 
                else:
                    break
 ```
 Starting at the second point, which is the first node traveled to, the benefit of switching two nodes on the path is
 searched.  If the cost of this test is less than the incumbent value, then the new incumbent value is this minimized
 path.  For this test a beginning path is found using the Branch and Bround method with no backtracking or searching.  
 This is for comparison and to see if a more optimal path can be found.  An arbitrary path could also be used as well
 as long as the path starts and ends at the same location.  The two-opt function is then used to find a smaller path.
 The time to take the first path was 310.06 seconds, around five minutes at a cost of 34.60.  The time for the two-opt
 search was 383.80 around six minutes at a cost of 30.92.  This was an improvement overall at finding a minimum 
 feasible path.  The tests were run on a random asymmetric distance matrix for 300 locations.  
            
