class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def has_cycle(self, head):
        s = head
        f = head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False

def starting_point(self, head):
    if not head or not head.next:
        return None

    # Detect if cycle ================
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # Cycle detected
            break
    else:
        return None  # No cycle found

    # Find the starting point ============
    fast = head
    while fast != slow:
        slow = slow.next
        fast = fast.next

    return fast
