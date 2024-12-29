from typing import List

# TIPS FOR INTERVIEW:
    # equal is overlap here? YES
    # ask if sorted or not?

# Approach: keep track of last added, if it overlaps with curr, modify its end = max of ends of both

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort by start time
        intervals.sort()

        result = [intervals[0]]

        # add first here to avoid
        # if not result condition in loop

        for start, end in intervals:
            lastEnd = result[-1][1]

            # if overlap - equal is overlap
            if start <= lastEnd:
                result[-1][1] = max(lastEnd, end)
            else:
                result.append([start, end])

        return result
