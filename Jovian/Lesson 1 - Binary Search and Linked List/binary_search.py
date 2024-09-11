def linear_search(nums, target):
    position = 0
    while position < len(nums):
        if nums[position] == target:
            return position
        position += 1
    return -1


def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = nums[mid]

        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)

        if mid_number == target:
            return mid
        elif mid_number > target:
            hi = mid - 1
        elif mid_number < target:
            lo = mid + 1

    return -1


print("------------------")
array = [1, 2, 6, 6, 6, 7, 8]
target = 6
result = binary_search(array, target)
print(result)


# using recursion
def recursive_binary_search(nums, target, lo, hi):
    if lo > hi:
        return -1
    if lo <= hi:
        mid = (lo + hi) // 2
        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", nums[mid])
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return recursive_binary_search(nums, target, lo, mid - 1)
        else:
            return recursive_binary_search(nums, target, mid + 1, hi)
    return -1


print("------------------")
result_new2 = recursive_binary_search(array, target, 0, len(array) - 1)
print(result_new2)


# returns first occurrence of target in the list

def test_location(nums, target, mid):
    mid_number = nums[mid]
    print("mid:", mid, ", mid_number:", mid_number)
    if mid_number == target:
        if mid - 1 >= 0 and nums[mid - 1] == target:
            return "left"
        else:
            return "found"
    elif mid_number > target:
        return "left"
    else:
        return "right"


def optimised_binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        print("lo:", lo, ", hi:", hi)
        mid = (lo + hi) // 2

        # condition
        result = test_location(nums, target, mid)

        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        elif result == "right":
            lo = mid + 1
    return -1


print("------------------")
result_new = optimised_binary_search(array, target)
print(result_new)


# first and last position - in O(log N)


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


print("------------------")
array2 = [5, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 10]
print(first_and_last_position(array2, 7))
