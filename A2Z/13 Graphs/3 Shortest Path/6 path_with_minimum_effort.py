# Input: heights =
# [[1,2,2],
#  [3,8,2],
#  [5,3,5]]
# Output: 2
# Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.


"""
Intution:
- Dijkstra keeps track of the minimum effort path (distance) to each node, so we can use it
- When we reach the destination (bottom right cell), we return the difference = max effort on that path
- We are using a PQ, so we always pop the smallest effort path, so when we reach destination, there is no better path. 
- All those after are worse (PQ pops the minimum diff tuple).
- So we can stop when we reach the destination.
"""

from queue import PriorityQueue

# TC = O (E * log V) ----> same as dijkstra
def minimumEffortPath(heights):
    """
    :type heights: List[List[int]]
    :rtype: int
    """
    n = len(heights)
    m = len(heights[0])

    # initialize with inf
    dist = [[float('inf')]*m for _ in range(n)]
    dist[0][0] = 0
    visited = set()
    
    q = PriorityQueue()
    q.put((0,0,0))

    directions = [(0,1),(0,-1),(1,0),(-1,0)]

    while not q.empty():
        diff, r, c = q.get()

        # reach destination --> return diff
        if r == n-1 and c == m-1:
            return diff
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr in range(n) and nc in range(m):
                # new effort = max of current diff & diff of parent node
                newEffort = max(abs(heights[nr][nc]-heights[r][c]), diff)
                # if better
                if newEffort < dist[nr][nc]:
                    dist[nr][nc] = newEffort
                    q.put((newEffort, nr, nc))
        
    return 0

