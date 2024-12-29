# return minimum number of removals to make non-overlapping
# similar appraoch to N meetings one room


def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])  # sort by end time
    n = len(intervals)
    lastEnd = intervals[0][1]
    count = 1  # count of non-overlapping intervals

    for start, end in intervals[1:]:
        if start >= lastEnd:
            count += 1
            lastEnd = end

    # minimum removals needed
    return n - count
