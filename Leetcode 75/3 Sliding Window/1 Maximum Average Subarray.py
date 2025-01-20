class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # initial window
        window_sum = sum(nums[:k])
        max_sum = window_sum


        for i in range(k, len(nums)):
            # to avoid recalculating sum each time, maintain window sum
            # removing left most and adding new ele
            window_sum += (- nums[i - k] + nums[i])
            max_sum = max(max_sum, window_sum)

        return max_sum / k
