import heapq


# TC = O(n log n)
# SC = O(k)
class Solution:
    def maxScore(self, nums1, nums2, k):
        # pair nums2 and nums1 and sort by nums2 (descending order)
        pairs = sorted(zip(nums2, nums1), reverse=True, key=lambda x: x[0])

        max_score = 0
        current_sum = 0
        min_heap = []

        for num2, num1 in pairs:
            # 1. add nums1 element to the heap and update the sum
            # 2. if heap exceeds size k, remove the smallest element
            # 3. if heap has size k, calculate the score
            heapq.heappush(min_heap, num1)
            current_sum += num1

            if len(min_heap) > k:
                current_sum -= heapq.heappop(min_heap)

            if len(min_heap) == k:
                max_score = max(max_score, current_sum * num2)

        return max_score
