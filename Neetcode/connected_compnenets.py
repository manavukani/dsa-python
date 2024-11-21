from typing import (
    List,
)

class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n 

        def find(node):
            p = node
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p 
        
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)

            if p1 == p2:
                return 0
            else:
                if rank[p1] >= rank[p2]:
                    rank[p1] += rank[p2]
                    par[p2] = p1 
                elif rank[p1] < rank[p2]:
                    rank[p2] += rank[p1]
                    par[p1] = p2 
                return 1
        
        res = n
        for node1, node2 in edges:
            res -= union(node1, node2)

        return res
