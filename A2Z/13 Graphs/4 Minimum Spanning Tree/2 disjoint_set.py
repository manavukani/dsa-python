# NEED: DFS/BFS for multiple components takes O(V+E)
# Used in dynamic graphs, cause of high speed

"""
TC: 
- find : O(4 * alpha) ==> O(const)
- union: O(4 * alpha) ==> O(const)

Alpha is very small


Why Smaller attach to larger?
- for compressing the new tree structure
- compressing -> faster findParent operation


"""


class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)  # stores the rank of the node i
        self.parent = list(range(n + 1))  # initially, each node is its own parent
        self.size = [1] * (n + 1)  # size of set to which node i belongs

    def findParent(self, node):
        # base case - node = parent of itself
        if node == self.parent[node]:
            return node
        # path compression, call recursively to find parent of parent
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

        # # iterative
        # if node == self.parent[node]:
        #     return node
        # p = node
        # while p != self.parent[p]:
        #     self.parent[p] = self.parent[self.parent[p]]
        #     p = self.parent[p]
        # return p

    def unionByRank(self, node1, node2):
        """
        rank only updated (increase) when we merge 2 nodes with same rank
        """
        # ultimate parents / representative of set
        p1 = self.findParent(node1)
        p2 = self.findParent(node2)

        # both have same parent, already in same set
        if p1 == p2:
            return

        # connect smaller rank node to larger rank node -- updated parent
        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        # same rank
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1

    # NOTE: Use size, more intuitive. (Don't use both together, lol)

    def unionBySize(self, node1, node2):
        p1 = self.findParent(node1)
        p2 = self.findParent(node2)

        if p1 == p2:
            return

        # attach the smaller set under the larger set
        if self.size[p1] < self.size[p2]:
            self.parent[p1] = p2
            self.size[p2] += self.size[p1]  # Update the size of the new set each time
        else:
            self.parent[p2] = p1
            self.size[p1] += self.size[p2]  # Update the size of the new set each time


ds = DisjointSet(7)
ds.unionBySize(1, 2)
ds.unionBySize(2, 3)
ds.unionBySize(4, 5)
ds.unionBySize(6, 7)
ds.unionBySize(5, 6)

print(ds.findParent(3) == ds.findParent(7))
ds.unionBySize(3, 7)
# ds.unionBySize(3, 7)
print(ds.findParent(3) == ds.findParent(7))
