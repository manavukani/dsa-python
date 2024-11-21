def validTree(n, edges):
    if not n:
        return True
    
    adj = {i:[] for i in range(n)}
    
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)
    
    visited = set()
    
    def dfs(i, prev):
        if i in visited:
            return False # loop

        # if new found
        visited.add(i)
        for j in adj[i]:
            # ignore the prev neighbor
            if j == prev:
                continue
            # check for other, now prev is current (i)
            if not dfs(j, i):
                return False
        
        return True
    
    # if dfs for all nodes from 0 and all nodes covered
    return dfs(0, -1) and n == len(visited)


print(validTree(5, [[0,1],[0,2],[0,3],[1,4]])) # true
