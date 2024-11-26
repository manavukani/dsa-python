# ip - sorted input array

# brute - O(n^2)
# binary search - O(nlogn)
# hash map - O(n), SC = O(n)

# 2 pointers - O(n), SC = O(1)
class Solution:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []
