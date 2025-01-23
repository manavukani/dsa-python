from collections import deque

# better with deque - memory utilization reduced
class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        # till first request is older than 3000ms, pop it
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft() # O(1) 
        # append the new request
        self.requests.append(t)

        return len(self.requests)


# if asked not to remove older requests, then we can use list instead of deque
class RecentCounter:
    def __init__(self):
        self.records = []
        self.start = 0

    def ping(self, t: int) -> int:
        self.records.append(t)
        while self.records[self.start] < t - 3000:
            self.start += 1
        return len(self.records) - self.start
