# TODO: at each step, start is multiplied with any number in the array and then mod operation with 100000 is done to get the new start.
# output: find the minimum steps in which end can be achieved starting from start. if not possible, return -1.

'''
INTUTION:
- similar to shortest path, check for all nei (all the elements in arr)
- if we encounter same val with more steps we ignore repeating calculation, not push to queue
- if found same val with less steps, we add to dict and queue
- dict is better than array of length 10**5, cause array will be sparse
- since we only move 1 step each time, no need to PQ
'''

from collections import deque

class Solution:
    def minimumMultiplications(self, arr, start, end):
        # Edge case
        if start == end:
            return 0

        MOD = 100000
        q = deque()
        q.append((start, 0))  # (current value, steps taken)
        
        dist = {}
        dist[start] = 0

        while q:
            val, steps = q.popleft()

            # checking all nei
            for ele in arr:
                num = (ele * val) % MOD  # next number
                
                if num not in dist or steps + 1 < dist[num]:
                    dist[num] = steps + 1
                    
                    # If we reach the end, return the steps
                    if num == end:
                        return steps + 1
                    
                    q.append((num, steps + 1))

        # unreachable, return -1
        return -1
