# given hand where hand[i] is the value written on the ith and groupSize
# divide hands in size = groupSize and each card have consecutive increasing numbers
# if possible return True, else False


from collections import Counter
import heapq


# Sorting --> O(N log N)
def with_sorting(hand, groupSize):

    # feasibility check
    if len(hand) % groupSize:
        return False

    count = Counter(hand)  # val -> freq

    # starting from the smallest available card and move up
    hand.sort()
    for num in hand:
        if count[num]:
            # check for next consecutive cards to form a group
            for i in range(num, num + groupSize):
                # if any missing, return False
                if not count[i]:
                    return False
                # remove used cards, decrement freq
                count[i] -= 1
    return True




# Min Heap ---> O(N log N)
def with_minHeap(hand, groupSize):
    if len(hand) % groupSize != 0:
        return False

    count = {}
    for card in hand:
        count[card] = 1 + count.get(card, 0)

    minHeap = list(count.keys())
    heapq.heapify(minHeap)

    while minHeap:
        first = minHeap[0]  # top -- smallest

        # check for consecutive ele to form group
        for i in range(first, first + groupSize):
            if i not in count:
                return False

            # remove used cards, decrement freq
            count[i] -= 1

            # IMP CHECK <-----------
            if count[i] == 0:
                # check if any ele other than smallest has become 0 freq
                # there will be a gap
                if i != minHeap[0]:
                    return False

                else:
                    heapq.heappop(minHeap)
    return True

print(with_minHeap([1, 2, 3, 6, 4, 5, 3, 7, 8], 3))

"""
eg:  freq. of 2 = 0, but minH[0] (top elemtn - smallest) is 1, so there will be gap --> 1 ___ 3
      not needed to iterate further, return False
"""
