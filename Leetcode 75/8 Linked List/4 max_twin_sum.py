class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# TC = O(N)
# SC = O(1)
class Solution:
    def pairSum(self, head):
        # find the cnter
        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the 2nd part
        curr = slow.next
        prev = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        # simultaneously itertate both, keeping track of max sum
        first = head
        second = prev

        max_sum = 0
        while first and second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum
