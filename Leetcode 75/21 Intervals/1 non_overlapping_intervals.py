class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort()
        erase = 0
        prevEnd = intervals[0][1]  # end of 1st interval

        # no need to check first, start from 2nd
        for s, e in intervals[1:]:
            # as expected, updated prevEnd
            if s >= prevEnd:
                prevEnd = e

            # OVERLAP FOUND!
            # greedily remove interval which ends first
            # there is less chance it will overlap with future ones
            else:
                erase += 1
                prevEnd = min(prevEnd, e)

        return erase
