# ===================== Brute Force =====================
# TC = O(n*k)
# SC = O(n)
def brute(arr, k):
    n = len(arr)
    res = []
    # we iterate till n-k
    for i in range(n-k+1):
        res.append(max(arr[i:i+k]))
    return res


# ===================== Using Heap =====================
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
=====================   Using Deque  =====================
===================== TC = SC = O(n) =====================

- When shifting window, push new element from rear of de-queue
- Every time before entering new element, first check element present at the front is out of bounds of our present window size.
- If so, pop that out.
- Check from rear that the element present is smaller than the incoming element. If yes, there's no point storing them, pop them out.
- The element present at the front would be our largest element.


IF NOT UNDERSTAND, SEE NEETCODE 150 FOLDER -> SLIDING WINDOW
'''
from collections import deque
def using_deque(arr, k):
    dq = deque()  # index
    res = []
    for i in range(len(arr)):
        # if element at front of queue (bottom) is
        # out of bounds (beyond window len), pop
        if dq and dq[0] <= i - k:
            dq.popleft() # Remove indices that are out of the window
        
        # if element at end of queue (top) is smaller than curr ele, pop
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop() # Remove indices whose corresponding values are less than nums[i]
        
        # add curr ele idx
        dq.append(i) # Add the current index to the deque
        
        # ensures we have reached window size, since we start from 0
        if i >= k - 1:
            res.append(arr[dq[0]])  # Max element is at the front of the deque
    return res


input = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(using_deque(input, k))  # [3, 3, 5, 5, 6, 7]
