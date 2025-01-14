# hint: remember where i am coming from

from queue import PriorityQueue

# TC = O(E log V ) + O(V) -------> dijkstra + loop for path
# SC = O(V)
def dijkstra_path(adj, src, dest):
    # remember the parent
    parent = [-1] * len(adj)
    distance = [float('inf')] * len(adj)
    # initiate values for source
    distance[src] = 0
    parent[src] = src

    q = PriorityQueue()
    q.put((0, src))

    while not q.empty():
        dist, node = q.get()

        for nei in adj[node]:
            neiNode = nei[0]
            edgeWt = nei[1]
            if dist + edgeWt < distance[neiNode]:
                distance[neiNode] = dist + edgeWt
                parent[neiNode] = node
                q.put((distance[neiNode], neiNode))
    
    # check if reached dest
    if distance[dest] == float('inf'):
        return -1
    
    # finding the path -- start from dest and go up till we reach a that's node is parent of itself
    path = []
    curr = dest
    while parent[curr] != curr:
        path.append(curr)
        curr = parent[curr]
    # loop breaks when we reach source, add it
    path.append(src)
    return path[::-1]

