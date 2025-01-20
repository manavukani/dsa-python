class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum, rsum = 0, sum(nums)

        # decrement the rsum and check if equal
        # else increment the lsum and move to next idx
        for idx, ele in enumerate(nums):
            rsum -= ele
            if lsum == rsum:
                return idx
            lsum += ele

        return -1