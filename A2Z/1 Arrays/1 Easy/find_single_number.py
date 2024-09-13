def find_single(nums):
    xor = 0
    for i in nums:
        xor ^= i
    return xor