# Xor of any two num gives the difference of bit as 1 and same bit as 0

class Solution:
    def singleNumber(self, nums):
        xor = 0
        for n in nums:
            xor ^= n
        return xor
