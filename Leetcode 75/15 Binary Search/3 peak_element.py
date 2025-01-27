class Solution:
    def findPeakElement(self, nums):
        l = 0
        h = len(nums) - 1
        while h > l:
            mid = (l + h) // 2
            # +ve slope, peak on right
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            # -ve slope slope, peak on left
            # peak could include the mid element in the descending case
            # so keep mid in search space
            else:
                h = mid
        return l
