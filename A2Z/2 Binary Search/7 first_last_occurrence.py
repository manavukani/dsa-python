# sorted array of N integers
# find the index of the last occurrence of the target key.
# If the target is not found then return -1.


# O(n)
def brute(arr, target):
    first, last = -1, -1
    for i in range(len(arr)):
        if arr[i] == target:
            if first == -1:
                first = i
            last = i
    return first, last

# 2 * O(log n)


def lower_bound_upper_bound():
    '''
    can use these to find the first and last occurrence
    2   4   6    8   8   8   11   13
    i   ii  iii  iv  v   vi  vii  viii

    target = 8

    lower bound (arr[i] >= target) => iv => first occurrence posn = lower bound
    upper bound (arr[i] > target) => vii => last occurrence posn = upper bound - 1


    some interviewers may not know lb & ub so might ask for binary

    '''
    pass


def binary(arr, target):
    def first_occurrence(arr, target):
        first = -1
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            # found
            if arr[mid] == target:
                first = mid
                high = mid - 1  # finding first so go left
            # not found
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1  # when arr[mid] > x
        return first

    def last_occurrence(arr, target):
        last = -1
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            # found
            if arr[mid] == target:
                last = mid
                low = mid + 1  # finding last so go right
            # not found
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1  # when arr[mid] > x
        return last

    return first_occurrence(arr, target), last_occurrence(arr, target)


array1 = [2, 4, 6, 8, 8, 8, 11, 13]  # (3, 5)
print(binary(array1, 8))


# -------------------- EXTRA FROM JOVIAN --------------------
# SAME BUT USING CONDITION AS HELPER FUNCTION
def first_and_last_position(nums, target):

    def binary_search(lo, hi, condition):
        while lo <= hi:
            mid = (lo + hi) // 2
            result = condition(mid)
            if result == "found":
                return mid
            elif result == "left":
                hi = mid - 1
            else:
                lo = mid + 1
        return -1

    def get_first_position(nums, target):

        def condition(mid):
            if nums[mid] == target:
                if mid > 0 and nums[mid - 1] == target:
                    return "left"
                else:
                    return "found"
            elif nums[mid] > target:
                return "left"
            else:
                return "right"

        return binary_search(0, len(nums) - 1, condition)

    def get_last_position(nums, target):

        def condition(mid):
            if nums[mid] == target:
                if mid < len(nums) - 1 and nums[mid + 1] == target:
                    return "right"
                else:
                    return "found"
            elif nums[mid] > target:
                return "left"
            else:
                return "right"

        return binary_search(0, len(nums) - 1, condition)

    return get_first_position(nums, target), get_last_position(nums, target)


print('------------------')
array2 = [5, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 10]
print(first_and_last_position(array2, 7))
