import heapq


# TC = O(m + k * log m) ==========> m = candidates, (m - heapify) + (k * log M - for loop)
# SC = O(m) =======> first and last m workers stored in pq


# using two PQ - for left and right candidates
class Solution:
    def totalCost(self, costs, k, candidates) -> int:
        # head_workers stores the first k workers.
        # tail_workers stores at most last k workers without any workers from the first k workers.
        # max - to avoid overlapping when 2 * candidates > n
        head_workers = costs[:candidates]
        tail_workers = costs[max(candidates, len(costs) - candidates) :]
        heapq.heapify(head_workers)
        heapq.heapify(tail_workers)

        answer = 0
        next_head, next_tail = candidates, len(costs) - 1 - candidates

        for _ in range(k):
            # If heap2 is empty or heap1 has smaller/equal value
            if not tail_workers or head_workers and head_workers[0] <= tail_workers[0]:
                answer += heapq.heappop(head_workers)

                # Only refill the queue if there are workers outside the two queues.
                # Add next element from left side if available
                if next_head <= next_tail:
                    heapq.heappush(head_workers, costs[next_head])
                    next_head += 1
            else:
                answer += heapq.heappop(tail_workers)

                # Add next element from right side if available
                if next_head <= next_tail:
                    heapq.heappush(tail_workers, costs[next_tail])
                    next_tail -= 1

        return answer


# single PQ/Heap
class Solution:
    def totalCost(self, costs, k, candidates) -> int:
        # push side as well to know where worker came from
        pq = []
        for i in range(candidates):
            pq.append((costs[i], "left"))
        for i in range(max(candidates, len(costs) - candidates), len(costs)):
            pq.append((costs[i], "right"))

        heapq.heapify(pq)

        answer = 0
        next_head, next_tail = candidates, len(costs) - 1 - candidates

        # only refill pq if there are workers outside.
        for _ in range(k):

            # edge case
            if not pq:
                break  # No more candidates to hire

            cost, side = heapq.heappop(pq)
            answer += cost

            if next_head <= next_tail:
                if side == "left":
                    heapq.heappush(pq, (costs[next_head], "left"))
                    next_head += 1
                else:
                    heapq.heappush(pq, (costs[next_tail], "right"))
                    next_tail -= 1

        return answer


""" my apporach -- using 2 heaps but everything is in terms of index (more complex)"""


class Solution:
    def totalCost(self, costs, k, candidates):
        n = len(costs)
        totalCost = 0

        # two heaps for first and last candidates
        heap1 = []
        heap2 = []

        left = candidates - 1
        right = n - candidates if n - candidates > left else left + 1

        # Add first and last 'candidates' elements
        for i in range(min(candidates, n)):
            heapq.heappush(heap1, (costs[i], i))
        for i in range(max(n - candidates, left + 1), n):
            heapq.heappush(heap2, (costs[i], i))

        for _ in range(k):
            # If heap2 is empty or heap1 has smaller/equal value
            if not heap2 or (heap1 and heap1[0][0] <= heap2[0][0]):
                cost, i = heapq.heappop(heap1)
                totalCost += cost
                # Add next element from left side if available
                if left + 1 < right:
                    left += 1
                    heapq.heappush(heap1, (costs[left], left))
            else:
                cost, i = heapq.heappop(heap2)
                totalCost += cost
                # Add next element from right side if available
                if right - 1 > left:
                    right -= 1
                    heapq.heappush(heap2, (costs[right], right))

        return totalCost


class Solution:
    def totalCost(self, costs, k, candidates):
        n = len(costs)
        totalCost = 0
        heap = []  # (cost, index, side)

        left_ptr = 0
        right_ptr = n - 1

        # To avoid overlapping when 2 * candidates > n
        front_candidates = min(candidates, n)
        back_candidates = min(candidates, n - front_candidates)

        # Push initial front and back candidates
        for _ in range(front_candidates):
            heapq.heappush(heap, (costs[left_ptr], left_ptr, "front"))
            left_ptr += 1
        for _ in range(back_candidates):
            heapq.heappush(heap, (costs[right_ptr], right_ptr, "back"))
            right_ptr -= 1

        for _ in range(k):
            if not heap:
                break  # No more candidates to hire

            cost, idx, side = heapq.heappop(heap)
            totalCost += cost

            # Push the next candidate from the same side
            if side == "front" and left_ptr <= right_ptr:
                heapq.heappush(heap, (costs[left_ptr], left_ptr, "front"))
                left_ptr += 1
            elif side == "back" and left_ptr <= right_ptr:
                heapq.heappush(heap, (costs[right_ptr], right_ptr, "back"))
                right_ptr -= 1

        return totalCost
