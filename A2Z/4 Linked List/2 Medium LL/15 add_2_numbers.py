class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# TC = SC = O(max(m,n))
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy

        carry = 0
        # !!!! EDGE CASE !!!!
        # CARRY can be there even when both list are over
        while l1 or l2 or carry:
            # value will be 0 in case of just carry
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
