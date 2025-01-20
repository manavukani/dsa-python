class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # place all non zero consecutively
        # place rest of zeroes

        insert = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert] = nums[i]
                insert+=1
        
        while insert < len(nums):
            nums[insert] = 0
            insert+=1