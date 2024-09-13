# 1, 1, 0, 1, 1, 1 => 3
def count(nums):
    count = 0
    max_val = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            count = 0
        max_val = max(max_val, count)
    return max_val


print(count([1, 1, 0, 1, 1, 1]))
