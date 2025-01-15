# input = node, connections
# condition = remove cables between 2 directly connected nodes, using it connect any pair of disconnected node to directly connect them
# output = minimum number of times you need to do this in order to make all the computers connected. If not possible, -1


# TC = SC = O(N)
# considering union-find to be (4 * alpha) ~ const
def solve(n, connections):
    # MST of n nodes, need n-1 edges
    if len(connections) < n - 1:
        return -1

    par = [i for i in range(n)]
    rank = [1] * n

    def find(node):
        if node == par[node]:
            return node
        par[node] = find(par[node])
        return par[node]

    def union(node1, node2):
        p1 = find(node1)
        p2 = find(node2)

        if p1 == p2:
            return

        if rank[p1] >= rank[p2]:
            rank[p1] += rank[p2]
            par[p2] = p1
        elif rank[p1] < rank[p2]:
            rank[p2] += rank[p1]
            par[p1] = p2

    # join all nodes
    for u, v in connections:
        union(u, v)

    # find unique parents after union find ---> gives number of components
    unique_parents = set(find(i) for i in range(n))
    k = len(unique_parents)

    # if all nodes are connected, no new connections needed
    if k == 1:
        return 0

    # new connections required will be k-1
    return k - 1


n = 6
connections = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
print(solve(n, connections))
