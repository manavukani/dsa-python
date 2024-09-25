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
    pass


arr = [1, 1, 2, 2, 2, 2, 2, 3]
target = 2
print(using_bounds(arr, target))
