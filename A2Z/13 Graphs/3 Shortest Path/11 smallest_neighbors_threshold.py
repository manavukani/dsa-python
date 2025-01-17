# input: edges: [[fromi, toi, weighti].....], n = no of cities, threshold
# output: city with smallest number of cities reachable and whose distance is at most distanceThreshold
# If there are multiple such cities, return the city with the greatest number.

from Queue import PriorityQueue
class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
    
        adj = [[] for _ in range(n)]
        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))
        
        # no. of cities reachable from src within threshold
        def helper(src):
            q = PriorityQueue()
            q.put((0, src))
            dist = [float('inf')]*n
            dist[src] = 0

            while not q.empty():
                cur_dist, node = q.get()

                if cur_dist > dist[node]:
                    continue

                for nei, wt in adj[node]:
                    new_dist = cur_dist + wt
                    if new_dist < dist[nei] and new_dist <= distanceThreshold:
                        dist[nei] = new_dist
                        q.put((new_dist, nei))

            # total cities reachable - self
            return sum(d <= distanceThreshold for d in dist) - 1

        res = 0
        lower_limit = n

        for src in range(n):
            cities_in_range = helper(src)
            # ensures for tie city with the largest index is selected, coz loop is increasing.
            if cities_in_range <= lower_limit:
                lower_limit = cities_in_range
                res = src

        return res
