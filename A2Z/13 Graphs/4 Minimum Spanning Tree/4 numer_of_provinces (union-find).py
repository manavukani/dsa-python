class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
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
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    res -= union(i, j)

        return res