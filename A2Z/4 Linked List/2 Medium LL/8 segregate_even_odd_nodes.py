class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


'''
INPUT: 1 -> 2 -> 3 -> 4 -> 5
OUTPUT: 1 -> 3 -> 5 -> 2 -> 4

'''

# TC = O(2N)
# SC = O(N)


def oddEvenList(head):
    # empty or single elements
    if not head or not head.next:
        return head

    curr = head
    arr = []

    # part 1
    while curr and curr.next:
        arr.append(curr.val)
        curr = curr.next.next

    # for odd length, we cannot access last element coz curr.next = None
    if curr:
        arr.append(curr.val)

    # part 2
    curr = head.next
    while curr and curr.next:
        arr.append(curr.val)
        curr = curr.next.next
    if curr:
        arr.append(curr.val)

    i = 0
    temp = head
    while temp:
        temp.val = arr[i]
        i += 1
        temp = temp.next

    return head

# space optimized - inplace
# TC = O(N), SC = O(1)
# https://youtu.be/qf6qp7GzD5Q
# skip 1 place for each next

#   1   2   3   4   5   6   7   8   9   None
#   O   E   O   E   O   E   O   E   O   x

def optimal(head):
    # null or single element
    if not head or not head.next:
        return head
    
    odd = head
    even = head.next
    evenHead = head.next
    
    while even and even.next:
        # connect alternate
        odd.next = odd.next.next
        even.next = even.next.next
        
        # move to next posn
        odd = odd.next
        even = even.next
    
    # at end, merging
    # oddHead @ head, evenHead @ end of odd
    odd.next = evenHead
    
    return head