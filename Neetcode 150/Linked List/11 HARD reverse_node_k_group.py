"""
eg1:
Input: head = [1,2,3,4,5,6], k = 3
Output: [3,2,1,6,5,4]

eg2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]


"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# TC = O(n)
# SC = O(1)
def reverseKGroup(self, head, k):
    dummy = ListNode(0, head)
    groupPrev = dummy

    def getKth(curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    while True:
        kth = self.getKth(groupPrev, k)
        if not kth:
            break
        groupNext = kth.next

        # reverse group
        prev, curr = kth.next, groupPrev.next
        while curr != groupNext:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        tmp = groupPrev.next
        groupPrev.next = kth
        groupPrev = tmp

    return dummy.next
