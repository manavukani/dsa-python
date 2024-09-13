def linear(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(linear(arr, 5))
