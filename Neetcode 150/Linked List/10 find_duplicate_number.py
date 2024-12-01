"""
INPUT: NUMS ARRAY, length = n+1
- all elements in range [1, n]
- only 1 number is repeated
OUTPUT: return repeated number
"""


# TC = O(nlogn)
# SC = O(n)
def sorting(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]
    return -1


# TC = O(n)
# SC = O(n)
def hash_set(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1


# TC = O(32*n)
# SC = O(1)
def bit_manipulation(nums):
    n = len(nums)
    res = 0
    for b in range(32):
        x = y = 0
        mask = 1 << b
        for num in nums:
            if num & mask:
                x += 1

        for num in range(1, n):
            if num & mask:
                y += 1

        if x > y:
            res |= mask
    return res


# SLOW FAST POINTER -----------> TORTOISE AND HARE

"""
     0 1 2 3 4
eg: [1,3,4,2,2]

len = n + 1 ====> but n different values
nums[i] in [1, n]

Think of this as graph:
- nums[0] = 1 ==> points at nums[1] = 3
- nums[1] = 3 ==> points at nums[3] = 2
- nums[2] = 4 ==> points at nums[4] = 2
- nums[3] = 2 ==> points at nums[2] = 4
- nums[4] = 2 ==> points at nums[2] = 4


- In term of linked list, it forms a LL with cycle:

Here: 1 => 3 => 2 <=> 4

- Cycle between 2 and 4
- Starting point of cycle is the duplicate
- Nothing will point at nums[0] since nums[i] is in [1,n]
- so there will always be a cycle with nums[0] where we can start and traverse


https://www.youtube.com/watch?v=wjYnzkAhcNk

"""


# TC = O(n)
# SC = O(1)
def optimal(nums):
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow
