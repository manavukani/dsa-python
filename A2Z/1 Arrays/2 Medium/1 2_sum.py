# 1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.
# 2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.

def brute(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]  # or return "YES"
    return []  # or return "NO"

# In the worst case(which rarely happens), the unordered_map takes O(N) to find an element. 
# In that case, the time complexity will be O(N2). If we use map instead of unordered_map, 
# the time complexity will be O(N* logN) as the map data structure takes logN time to find an element.
def brute_optimized(nums, target):
    hash_map = {}
    for i in range(len(nums)):
        remaining = target - nums[i]
        # check if remaining already exist
        if remaining in hash_map:
            return [i, hash_map[remaining]]
        # add current to hash map
        hash_map[nums[i]] = i
    return []

# ==== NEED TO SORT THE ARRAY ====
def two_pointer(nums, target):
    l = 0
    r = len(nums) - 1
    nums.sort()
    while l < r:
        if nums[l] + nums[r] == target:
            return "Yes"
        elif nums[l] + nums[r] < target:
            l += 1
        else:
            r -= 1

    return "No"


print(brute([2, 7, 11, 15], 9))  # [0, 1]
print(brute_optimized([2, 6, 5, 8, 11], 14))  # [1,3]
