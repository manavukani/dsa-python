# brute =====================
# TC = O(n*k)
# SC = O(n)
def brute(arr, k):
    n = len(arr)
    res = []
    # we iterate till n-k
    for i in range(n-k+1):
        res.append(max(arr[i:i+k]))
    return res


# Using Heap =====================
# TC = O(nlogn)
# SC = O(n)
import heapq
def using_heap(arr, k):
    heap = []
    output = []
    for i in range(len(arr)):
        heapq.heappush(heap, (-arr[i], i))
        if i >= k - 1:
            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            output.append(-heap[0][0])
    return output


'''
Using Deque ===========> Monotonicaly Decreasing DE-Queue

=> Maintain queue where the elements are in decreasing order
=> First element in queue corresponds to max element inside window
=> After each window slide, remove elements from end of queue until
last queue element > curr element, or the queue becomes empty.
=> Also remove first queue element if its not inside window anymore
=> Add the new window element to end of queue.


eg1: [8 7 6 9], k = 2

q = 8 7 => res = [8]
popleft 8
q = 7 6 => res = [8, 7]
popleft 7
since 9 > 6, we pop 6 and add 9
q = 9 => res = [8, 7, 9]


eg2: [2 1 4 5 3 4 1 2], k = 4

2 1 4 5 3 4 1 2
-------
q = 2 1
now 4 > 1, so we pop 1 and 2
q = 4
now 5 > 4, so we pop 4
q = 5 => res = [5] (since we have reached window size)
=============================
2 1 4 5 3 4 1 2
  -------
q = 5 3 => res = [5, 5]
=============================
2 1 4 5 3 4 1 2
    -------
q = 5 4 (since 3 < 4, we pop 3) => res = [5, 5]
=============================
2 1 4 5 3 4 1 2
      -------
q = 5 4 1 => res = [5, 5, 5]
=============================
2 1 4 5 3 4 1 2
        -------
we popleft 5 - out of bounds
we pop 1, since 2 > 1
q = 4 2 => res = [5, 5, 5, 4]

'''
# TC = SC = O(n)
from collections import deque
def using_deque(arr, k):
    output = []
    q = deque()  # index
    l = r = 0
    while r < len(arr):
        # non empty and last ele < curr element
        while q and arr[q[-1]] < arr[r]:
            q.pop()
        q.append(r)

        # if left val out of bounds => left idx > first ele in queue
        if l > q[0]:
            q.popleft()

        # EDGE CASE => if r+1 >= k, then only we start adding to output
        # since we start from 0, we need to add window len elements
        if (r + 1) >= k:
            output.append(arr[q[0]])
            l += 1
        r += 1


# input = [1, 3, -1, -3, 5, 3, 6, 7]
input = [2, 1, 4, 5, 3, 4, 1, 2]
k = 4
print(using_heap(input, k))