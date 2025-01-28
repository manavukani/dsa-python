class Solution:
    def findMinArrowShots(self, points):
        points.sort()
        arrow = 1
        prevEnd = points[0][1]  # end of 1st interval

        # no need to check first, start from 2nd
        for s, e in points[1:]:
            # no overlap - increase arrow
            if s > prevEnd:
                prevEnd = e
                arrow += 1

            # OVERLAP - remove balloon which ends first
            # 2nd can overlap in future with other
            else:
                prevEnd = min(prevEnd, e)

        return arrow
