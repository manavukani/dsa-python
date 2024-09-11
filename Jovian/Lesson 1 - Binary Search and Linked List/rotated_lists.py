"""

You are given list of numbers, obtained by rotating a sorted list an unknown number of times. 
Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. 
Your function should have the worst-case complexity of O(log N), where N is the length of the list. 
You can assume that all the numbers in the list are unique.

Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

We define "rotating a list" as removing the last element of the list and adding it before the first element. 
E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

"Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].

"""

# simple plain logic -
# If a list of sorted numbers is rotated k times, then the smallest number in the list ends up at position k (counting from 0).
# It is the only number in the list which is smaller than the number before it.


# brute force - O(N)
def linear_solve(nums):
    for position in range(1, len(nums)):
        if nums[position] < nums[position - 1]:
            return position
    return 0


# using binary search O(N)
def optimal_solve(nums):
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_num = nums[mid]

        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_num)

        if mid > 0 and nums[mid] < nums[mid - 1]:
            return mid
        elif nums[mid] < nums[hi]:
            hi = mid - 1
        else:
            lo = mid + 1

    return lo

print("rotation index:", optimal_solve([7, 8, 1, 3, 4, 5, 6]), "\n")
print("rotation index:", optimal_solve([1, 2, 3, 4, 5, -1, 0]), "\n")
print("rotation index:", optimal_solve([1, 2, 3, 4, 5]), "\n")
print("rotation index:", optimal_solve([5, 6, 9, 0, 2, 3, 4]), "\n")

# bonus 1 - use condition in Generic Binary Search Algorithm

# bonus 2 - handle repeating numbers (covered in bonus 4)

# bonus 3 - searching in rotated

# bonus 4 - rotated and sorted

# def check(nums):
#     return sum(a > b for a, b in zip(nums, nums[1:] + nums[:1])) <= 1