class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        L, R = 0, 0
        count = 0
        maxAns = 0

        while R < len(nums):
            # expand right pointer
            if nums[R] == 0:
                count += 1

            # shrink left if more than 1 zero is in it
            while count > 1:
                if nums[L] == 0:
                    count -= 1
                L += 1

            # maximum subarray length (subtract 1 for deleted ele)
            maxAns = max(maxAns, R - L)

            # expand the window
            R += 1
        return maxAns