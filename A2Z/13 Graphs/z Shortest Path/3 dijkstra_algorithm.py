from queue import PriorityQueue  # PREFFERED
import heapq

'''
Dijkstra Algo:
- start from source, initiate all dist as inf
- check for nei and if current dist + edge < nei dist, then update
- check for the smallest dist among all explored node --------- use of min-heap/priority queue
- do the same for it and keep updating

Limitations:
- does not work for negative weights
- also does not work for negative cycles

Reason:
- if we have a negative weight, we keep reducing the distance
- every traversal we will get a better distance
- this will fall into infinite loop
'''

# input - undirected weighted graph and source
# output = distance to source node

# TC = O(E * log(V))
# SC = O(V)
def dijkstra(adj, src):
    distance = [float("inf")] * len(adj)
    distance[src] = 0

    q = PriorityQueue()
    q.put((0, src))  # priority, val

    # NOTE: cannot use while q:
    #       because PriorityQueue is not iterable
    #       so does not evaluate to False when it is empty
    while not q.empty():
        dist, node = q.get()

        for nei in adj[node]:
            adjNode = nei[0]
            edgeWt = nei[1]
            # check if current + edge < nei distance, if so, update
            if dist + edgeWt < distance[adjNode]:
                distance[adjNode] = dist + edgeWt
                q.put((distance[adjNode], adjNode))

    return distance


adj = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]]

print(dijkstra(adj, 2))


# using heapq -- it is iterable but not thread safe like PriorityQueue
def dijkstra_heapq(adj, src):
    distance = [float("inf")] * len(adj)
    distance[src] = 0

    q = []
    heapq.heappush(q, (0, src))  # mimic priority queue

    while q:
        dist, node = heapq.heappop(q)

        for nei in adj[node]:
            adjNode, edgeWt = nei
            if dist + edgeWt < distance[adjNode]:
                distance[adjNode] = dist + edgeWt
                heapq.heappush(q, (distance[adjNode], adjNode))

    return distance

# using set
def dijkstra_set(adj, src):
    distance = [float("inf")] * len(adj)
    distance[src] = 0

    s = set()
    s.add((0, src))

    while s:
        dist, node = s.pop()

        for nei in adj[node]:
            adjNode, edgeWt = nei
            if dist + edgeWt < distance[adjNode]:
                distance[adjNode] = dist + edgeWt
                s.add((distance[adjNode], adjNode))

    return distance