# input: [[u,v,time].....] -> 2 nodes and time between both, n -> total nodes
# output: the number of ways to arrive from 0 to n - 1 in shortest time

"""
PLAIN DIJKSTRA: counting paths with min distance to dest. Won't work cause we cannot account for multiple paths through same node

MODIFIED WAY:
- keep track of 2 array
    1. ways => how many ways for each node we can reach with MINIMUM dist
    2. dist => minimum distance to reach that node (in this case TIME)
- add src node
- check for nei if new dist is less than current best, update & increment the ways for it & ADD TO QUEUE
- if same as current best, increment the ways for it, DO NOT ADD TO QUEUE
- MOST IMPPPP!!! - if a node has 'x' ways, and we go its nei. bring the 'x' ways to its nei also
- return the ways for last node
"""


from queue import PriorityQueue


# O(E log V)
def minimumWays(n, roads):
    # prepare the adj list
    adj = [[] for _ in range(n)]
    for u, v, time in roads:
        adj[u].append((v, time))
        adj[v].append((u, time))

    # 2 arrays
    ways = [0] * n
    dist = [float("inf")] * n

    # IMP
    ways[0] = 1
    dist[0] = 0

    q = PriorityQueue()
    q.put((0, 0))  # time, node

    while not q.empty():
        time, node = q.get()

        for nei, edgeWt in adj[node]:
            # new dist less than current best
            if time + edgeWt < dist[nei]:
                dist[nei] = time + edgeWt
                q.put((time + edgeWt, nei))
                ways[nei] = ways[node]  # IMPPPP - bring the # of ways of parent
            # new dist same as current best
            elif dist[nei] == time + edgeWt:
                ways[nei] = ways[nei] + ways[node]  # again IMP

    return ways[n - 1] % (10**9 + 7) # for LC


n = 7
roads = [
    [0, 6, 7],
    [0, 1, 2],
    [1, 2, 3],
    [1, 3, 3],
    [6, 3, 3],
    [3, 5, 1],
    [6, 5, 1],
    [2, 5, 1],
    [0, 4, 5],
    [4, 6, 2],
]
print(minimumWays(n, roads))