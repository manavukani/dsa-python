"""
Bellman Ford Algorithm
- COULD BE A FOLLOW UP QUESTION FOR DIJKSTRA

NEED:
- dijkstra fails when - negative edges
-                     - negative cycle (gets stuck in loop to minimize the path distance)
- helps detect negative cycles, but ONLY works in directed
- to implement for undirected, convert to directed (add edges to both sides with same wt.)

"""

"""
ALGO:
0. order of edges does not matter
1. relax all edges N-1 time sequentially (ie: N-1 iterations)
2. after N-1 iterations we will get shortest path distance from src to all other nodes

APPENDIX:
- Relax: if new distance is better than current best, update ---> dist[nei] = dis[node] + edgeWt
- Why N-1 iterations: even in worst case, ensures all 'N-1 edges' will be relaxed eventually
- How to detect negative cycle: If on Nth iteration, distance array is updated and values are reduced (cause at N-1 we get our shortest path)
"""


def bellman_ford(V, edges, src):
    dist = [float("inf")] * V
    dist[src] = 0

    for _ in range(V):  # for N-1 times
        for u, v, wt in edges:
            # reachable and better than current
            if dist[u] != float("inf") and dist[u] + wt < dist[v]:
                dist[v] = dist[u] + wt  # relax

    return dist


# TC = O(V*E) ---- more than Dijkstra (E logV) but works for -ve wt and cycles
# SC = O(V)
def detectCycle(V, edges, src):
    dist = [float("inf")] * V
    dist[src] = 0

    for _ in range(V):  # for N-1 times
        for u, v, wt in edges:
            # reachable and better than current
            if dist[u] != float("inf") and dist[u] + wt < dist[v]:
                dist[v] = dist[u] + wt  # relax

    # extra iteration to check negative cycle
    for u, v, wt in edges:
        # negative cycle if distance is still updated after N-1 iterations
        if dist[u] != float("inf") and dist[u] + wt < dist[v]:
            return -1

    # if no negative cycle, return dist
    return dist


V = 3
edges = [[0, 1, 5], [1, 0, 3], [1, 2, -1], [2, 0, 1]]
src = 2

print(detectCycle(V, edges, src))
