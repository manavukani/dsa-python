import heapq

# using constraint given - "At most 1000 calls will be made in total to popSmallest and addBack"
class MySolution:
    def __init__(self):
        self.infiniteSet = set(x for x in range(1, 1001))
        self.heap = [x for x in range(1, 1001)]

    def popSmallest(self) -> int:
        ele = heapq.heappop(self.heap)
        self.infiniteSet.remove(ele)
        return ele

    def addBack(self, num: int) -> None:
        if num not in self.infiniteSet:
            self.infiniteSet.add(num)
            heapq.heappush(self.heap, num)


# better solution --- more generalized and space optimized
# Instead of maintaining the entire range, just track the numbers added back in set and use min-heap for smallest
class SmallestInfiniteSet:

    def __init__(self):
        self.current = 1  # tracks smallest number not yet popped - lazy initialization (instead of whole 1000 nums)
        self.added_back = set()  # stores added back numbers
        self.heap = []

    def popSmallest(self) -> int:
        # check if there are any added-back numbers
        if self.heap:
            ele = heapq.heappop(self.heap)
            self.added_back.remove(ele)
            return ele
        else:
            self.current += 1
            return self.current - 1

    def addBack(self, num: int) -> None:

        if num < self.current and num not in self.added_back:
            heapq.heappush(self.heap, num)
            self.added_back.add(num)
