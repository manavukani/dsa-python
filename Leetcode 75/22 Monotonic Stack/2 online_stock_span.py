class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        print(self.stack)
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span


obj = StockSpanner()
print(obj.next(100))
print(obj.next(80))
print(obj.next(60))
print(obj.next(70))
print(obj.next(60))
print(obj.next(75))
print(obj.next(85))

'''

[] ---> 1
[(100, 1)] ---> 1
[(100, 1), (80, 1)] ---> 1
[(100, 1), (80, 1), (60, 1)] ---> 2
[(100, 1), (80, 1), (70, 2)] ---> 1
[(100, 1), (80, 1), (70, 2), (60, 1)] ---> 4
[(100, 1), (80, 1), (75, 4)] ---> 6

'''