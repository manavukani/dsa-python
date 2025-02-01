# houses are in circular pattern
# so we cannot pick both - first and last house


class Solution:
    def rob(self, nums):
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        # take max of - all except 0th, all except last
        return max(self.house_rob(nums[1:]), self.house_rob(nums[:-1]))

    def house_rob(self, nums):
        prev2 = 0
        prev = 0

        if not nums:
            return 0

        for n in nums:
            tmp = max(prev2 + n, prev)
            prev2 = prev
            prev = tmp

        return prev
