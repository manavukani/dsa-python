# TAKEAWAY 1:
# cant store in terms of distance -- edge cases fails
# we cannot use dijkstra because we need to focus on stops
# we store in terms of stops

# TAKEAWAY 2:
# we can use a priority queue to store the stops, node, cost
# but stops increases by 1 each time, increase is constant
# so we can use a normal queue for better time complexity (avoid log N for PQ get)

from collections import deque


def findCheapestPrice(n, flights, src, dst, k):
    """
    :type n: int
    :type flights: List[List[int]]
    :type src: int
    :type dst: int
    :type k: int
    :rtype: int
    """
    # construct adj
    adj = [[] for _ in range(n)]
    for start, end, cost in flights:
        adj[start].append((end, cost))

    # cost to reach each node
    dist = [float("inf")] * n
    dist[src] = 0

    # cost/distance
    q = deque()  # stops, node, cost
    q.append((0, src, 0))

    while q:
        stops, node, cost = q.popleft()

        if stops > k:
            continue

        for neighbor, edgeWt in adj[node]:
            # if total cost to reach neighbor is less than current best cost
            if cost + edgeWt < dist[neighbor] and stops <= k:
                # update shortest cost to reach neighbor
                dist[neighbor] = cost + edgeWt
                # add neighbor to queue with incremented stops
                q.append((stops + 1, neighbor, cost + edgeWt))

    if dist[dst] == float("inf"):
        return -1

    return dist[dst]
