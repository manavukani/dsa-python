# input: times = [(ui, vi, wi),....] -- u --> v with wt = wi, n = nodes (1 to n), k = src
# output: minimum time needed for signal to reach all node from k, if not possible return -1

'''
INTUTION:
- we need to minimize the max time taken
- use PQ and find shortest distance (time taken) to each node from src using dijkstra
- PQ/min-heap based on time, pick smaller time first
- check for each node in PQ, if any nei has better time than current cur stored in array
'''

import heapq

# TC = O(E log V)    ---->    (same as normal dijkstra)
def networkDelayTime(times, n, k):
    """
    :type times: List[List[int]]
    :type n: int
    :type k: int
    :rtype: int
    """
    # convert edges to adj list
    adj = [[] for _ in range(n+1)] # 1-based indexing
    for u,v,wt in times:
        adj[u].append((v, wt))
    
    min_heap = [(0, k)]  # (current time, node)

    dist = [float('inf')]*(n+1)
    dist[k] = 0

    while min_heap:
        time, node = heapq.heappop(min_heap)

        # redundancy check
        if time > dist[node]:
            continue

        for nei, edgeWt in adj[node]:
            new_time = time + edgeWt
            # shorter path to nei is found
            if new_time < dist[nei]:
                dist[nei] = new_time
                heapq.heappush(min_heap, (new_time, nei))
    
    # time needed for all nodes to recieve signal = max time for any node
    max_time = max(dist[1:])  # ignore the 0th index
    return -1 if max_time == float('inf') else max_time
