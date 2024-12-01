# Definition for singly-linked list.

"""
INPUT: 1, 2, 3, 4, 5, 6
OUTPUT: 1, 6, 2, 5, 3, 4

REORDER: 0, n-1, 1, n-2, 3, n-3, .......
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# TC = O(n)
# SC = O(1)
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        # ========= find middle
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # middle @ slow
        # ========= split both half
        # init 2nd half
        second = slow.next
        # splitting
        slow.next = None

        # ========= reverse 2nd half
        prev = None
        while second:
            nextNode = second.next
            second.next = prev
            prev = second
            second = nextNode

        # prev @ head (reversed LL)

        # ========= merge both alternatively
        first = head
        second = prev

        # both equal or second shorter
        while second:
            tmp1 = first.next
            tmp2 = second.next

            # insert "second" between "first" and "first.next"
            first.next = second
            second.next = tmp1

            # shift pointers
            first, second = tmp1, tmp2
