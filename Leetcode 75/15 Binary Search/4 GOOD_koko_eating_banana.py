# piles = array of bananas, with array[i] = # bananas in that pile
# h = max time available (guard will return)
# return k - bananas per hour eaten, such that all banana are eaten but as slowly as possible


import math


class Solution:
    def minEatingSpeed(self, piles, h):
        # solution will be from 1 ...... max value in piles
        low = 1
        high = max(piles)

        res = high  # worst case

        while low <= high:
            k = (high + low) // 2
            # find hours for given k
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = min(res, k)
                # smaller possible?
                high = k - 1
            else:
                low = k + 1

        return res
