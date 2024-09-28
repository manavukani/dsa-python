# sorted array containing N integers and a number X,
# you have to find the occurrences of "target" in the given array.

# [2, 2 , 3 , 3 , 3 , 3 , 4]
# target = 3
# output = 4
import bisect


def brute(arr, target):
    return arr.count(target)


def using_bounds(arr, target):
    left = bisect.bisect_left(arr, target)
    right = bisect.bisect_right(arr, target)
    return right - left


def using_binary_search(arr, target):
    '''

    result = last occurrence - first occurrence + 1

    '''
    def firstOccurrence(arr, n, k):
        low = 0
        high = n - 1
        first = -1

        while low <= high:
            mid = (low + high) // 2
            # maybe an answer
            if arr[mid] == k:
                first = mid
                # look for smaller index on the left
                high = mid - 1
            elif arr[mid] < k:
                low = mid + 1  # look on the right
            else:
                high = mid - 1  # look on the left

        return first


    def lastOccurrence(arr, n, k):
        low = 0
        high = n - 1
        last = -1

        while low <= high:
            mid = (low + high) // 2
            # maybe an answer
            if arr[mid] == k:
                last = mid
                # look for larger index on the right
                low = mid + 1
            elif arr[mid] < k:
                low = mid + 1  # look on the right
            else:
                high = mid - 1  # look on the left

        return last


    def firstAndLastPosition(arr, n, k):
        first = firstOccurrence(arr, n, k)
        if first == -1:
            return (-1, -1)
        last = lastOccurrence(arr, n, k)
        return (first, last)


    first, last = firstAndLastPosition(arr, len(arr),target)
    if first == -1:
        return 0
    return last - first + 1
        


arr = [1, 1, 2, 2, 2, 2, 2, 3]
target = 2
print(using_bounds(arr, target))
