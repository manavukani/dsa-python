class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        curr = head
        prev = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            # move ahead
            prev = curr
            curr = nextNode
        return prev
