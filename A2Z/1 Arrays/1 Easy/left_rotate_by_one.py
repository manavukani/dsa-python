# First element is present at the last index of the array
# Store the element at first index and then shift all the elements towards the left
# Put the stored element at the last index

def solve(nums):
    first = nums[0]
    n = len(nums)
    # till n-1 to prevent segmentation fault -> runtime error
    for i in range(n-1):
        nums[i] = nums[i+1]
    nums[-1] = first
    return nums


print(solve([1, 2, 3, 4, 5]))
