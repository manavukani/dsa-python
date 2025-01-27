import heapq
import random


class Solution:
    def findKthLargest(self, nums, k):
        nums = [-x for x in nums]
        heapq.heapify(nums)  # O(n)
        for _ in range(k):  # O(k log n)
            ele = heapq.heappop(nums)

        return -ele


# better --> avg. theta(n) but O(n^2)
class Solution:
    def findKthLargest(self, nums, k):
        pivot = random.choice(nums)
        left = [num for num in nums if num > pivot]
        mid = [num for num in nums if num == pivot]
        right = [num for num in nums if num < pivot]

        length_left = len(left)
        length_right = len(right)
        length_mid = len(mid)
        if k <= length_left:
            return self.findKthLargest(left, k)
        elif k > length_left + length_mid:
            return self.findKthLargest(right, k - length_mid - length_left)
        else:
            return mid[0]
