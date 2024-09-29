# You need to find the length of the longest sequence which contains the consecutive elements.

# [100, 200, 1, 3, 2, 4] => 4
# [100,4,200,1,3,2] => 3
# [0,3,7,2,5,8,4,6,0,1] => ??


# N^2
def brute(nums):
    def linear_search(nums, target):
        for i in nums:
            if i == target:
                return True
        return False
    
    longest = 1
    for i in range(len(nums)):
        x = nums[i]
        cnt = 1
        # check for every next element is there is i+1
        while linear_search(nums, x+1):
            x += 1
            cnt += 1
        longest = max(longest, cnt)
    return longest

# O(N log N) => with sorting
# since we are distorting array, interviewer might ask to do without sorting
def solve(nums):
    nums.sort()
    maxCount = 0
    stack = []
    for i in range(len(nums)):
        if not stack or stack[-1] == nums[i] - 1:
            stack.append(nums[i])
            # print(stack, nums[i])
        elif stack[-1] == nums[i]:
            # print(stack, nums[i])
            continue
        elif stack[-1] != nums[i] - 1:
            maxCount = max(maxCount, len(stack))
            stack = [nums[i]]
    maxCount = max(maxCount, len(stack))
    return maxCount

# using set without sort => O(N)
# coz time complexity of searching in a set is O(1)
# worst case O(N^2) due to collision
def better(nums):
    if len(nums) == 0:
        return 0

    maxCount = 1
    
    st = set()
    # put all the array elements into set
    for i in range(len(nums)):
        st.add(nums[i])

    # Find the longest sequence
    for num in st:
        # check if 'num' is a starting number => previous does not exist
        if num - 1 not in st:
            # find consecutive numbers
            cnt = 1
            x = num
            while x + 1 in st:
                x += 1
                cnt += 1
            maxCount = max(maxCount, cnt)
    return maxCount

print(solve([100, 200, 1, 3, 2, 4]))
print()

print(solve([100,4,200,1,3,2,1,1]))
print()

print(solve([0,3,7,2,5,8,4,6,0,1]))
print()
