class Solution():
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = float('inf') # first smallest
        second = float('inf') # second smallest
        # if we find number smaller than these 2. we have triplet

        for n in nums:
            # found new smallest, just update first
            # ensures if later found n > second, confirm triplet exists
            if n <= first:
                first = n
            # greater than smallest but less than second smallest
            elif n <= second:
                second = n
            # greater than both -> found triplet
            else:
                return True
        return False

        