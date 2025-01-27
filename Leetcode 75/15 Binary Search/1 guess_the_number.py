import random

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


# TC = O(log N)
class Solution:
    def guessNumber(self, n: int) -> int:
        # would be given, this is for testing
        def guess(num, target=random.randint(1, n)):
            print("Random int", target)
            if num == target:
                return 0
            elif num < target:
                return 1
            else:
                return -1

        low = 1
        high = n

        mid = (low + high) // 2

        while guess(mid) != 0:
            res = guess(mid)
            if res == 1:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2

        return mid


n = 10
s = Solution()
print(s.guessNumber(n))
