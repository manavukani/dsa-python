def naive(arr, dep):
    intersections = 1
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] <= arr[i] or dep[i] >= dep[j]:
                intersections += 1
    return intersections


"""
====================== NAIVE ====================
- count intersections for each of the interval with all others
- 4 cases
    1. arriving before, departing later
    2. arriving before, departing before
    3. arriving later, departing later
    4. both in between

TC = O(N^2)
SC = O(1)
"""


def naive(arr, dep):
    n = len(arr)
    max_count = 1
    for i in range(n):
        count = 1
        for j in range(i + 1, n):
            # arriving before, departing later
            # arriving late, departing before
            if (arr[i] >= arr[j] and arr[i] <= dep[j]) or (
                arr[j] >= arr[i] and arr[j] <= dep[i]
            ):
                count += 1
        max_count = max(max_count, count)
    return max_count


"""
==================== BETTER -- SORTING ==================
- sort both, easy to track trains arrived but not departed
- platforms required = difference in arrivals and departures

"""


def minimum_platforms(arr, dep):
    arr.sort()
    dep.sort()

    ans = 1
    count = 1
    i = 1
    j = 0
    while i < len(arr) and j < len(dep):
        # arrived before departure
        if arr[i] <= dep[j]:
            count += 1
            i += 1
        else:  # one platform can be reduced
            count -= 1
            j += 1
        ans = max(ans, count)
    return ans


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
print(naive(arr, dep))
print(minimum_platforms(arr, dep))
