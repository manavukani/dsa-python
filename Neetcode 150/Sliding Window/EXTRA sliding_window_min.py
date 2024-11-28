
# SLIDING WINDOW MINIMUM

'''
DEQUE METHOD ====> MONOTONIC INCREASING ORDER
TC = SC = O(n)

- we do the same as above, but instead of max, we maintain min
- queue in MONOTONIC INCREASING ORDER
- if new element is smaller than last element, we pop until empty or last element < curr element
- popleft if left element is out of bounds
- add new element to end of queue

eg: [2 1 4 5 3 4 1 2], k = 4

2 1 4 5 3 4 1 2
-------
q = 2
pop 2, since 1 < 2
q = 1 4 5 => res = [1]
=============================
2 1 4 5 3 4 1 2
  -------
pop 4 and 5 since curr = 3 < 4,5
q = 1 3 => res = [1, 1]
=============================
2 1 4 5 3 4 1 2
    -------
popleft 1
q = 3 4 => res = [1, 1, 3]
=============================
2 1 4 5 3 4 1 2
      -------
pop 3 and 4 since curr = 1 < 3,4
q = 1 => res = [1, 1, 3, 1]
=============================
2 1 4 5 3 4 1 2
        -------
q = 1 2 => res = [1, 1, 3, 1, 1]
'''

from collections import deque
def sliding_window_min(arr, k):
    output = []
    q = deque()
    l = r = 0
    while r < len(arr):
        # non empty and last ele > curr element
        while q and arr[q[-1]] > arr[r]:
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
    return output


input = [2, 1, 4, 5, 3, 4, 1, 2]
k = 4
print(sliding_window_min(input, k))