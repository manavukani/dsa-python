# find smallest index such that number at that index >= x
# arr[index] >= x

# 3 5 8 15 19
# x = 9 => ans = 3
# x = 8 => ans = 2

# x = 25 => ans = 5 (if not found return length of array)

# O(n)
def brute(arr, x):
    for i in range(len(arr)):
        if arr[i] >= x:
            return i
    return len(arr)


arr = [3, 5, 8, 15, 19]
# print(brute(arr, 9))


# O(log n)
def binary(arr, x):
    low = 0
    high = len(arr) - 1
    ans = len(arr)  # if nothing found return length of array

    while low <= high:
        mid = (low+high)//2
        if arr[mid] >= x:
            ans = mid  # maybe be an answer
            high = mid - 1
        else:
            low = mid + 1

    return ans


print(binary(arr, 9))

'''

CONTEXT: check striver video

bisect.bisect_left(a, x, lo=0, hi=len(a)) is the analog of std::lower_bound().

bisect.bisect_right(a, x, lo=0, hi=len(a)) is the analog of std::upper_bound().

Note: there is also a function bisect() which is an alias for bisect_right

'''

# ALSO CHECK 8 find_occurrences.py for use of bisect_left and bisect_right
