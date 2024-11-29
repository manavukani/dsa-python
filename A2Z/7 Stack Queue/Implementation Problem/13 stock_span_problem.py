'''
Design an algorithm that collects daily price quotes for some stock and
returns the span of that stock's price for the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward)
for which the stock price was less than or equal to the price of that day.

eg:

Input:
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output:
[null, 1, 1, 1, 2, 1, 4, 6]

'''

# ============== Brute force ==============
# O(n^2) -> for each element, check all previous elements and count the span


class BruteForce:
    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        self.arr.append(price)
        count = 1
        for i in range(len(self.arr)-2, -1, -1):
            if self.arr[i] <= price:
                count += 1
            else:
                break

        return count

# ============== Monotonic Stack - Previous Greater Element ==============
# TC = O(2N) - for each element, push and pop once
# SC = O(N) - max store N elements in stack

class StockSpanner:

    def __init__(self):
        self.stack = []  # val, idx
        self.idx = -1

    def next(self, price: int) -> int:
        self.idx += 1
        
        # monotonically decreasing stack of prices
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()  # pop all previous smaller elements
            
        # span = current idx - previous greater element idx
        if self.stack:
            ans = self.idx - self.stack[-1][1]
        # span = current idx + 1
        else:
            ans = self.idx + 1
        self.stack.append((price, self.idx))
        
        return ans
