class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:

            mergedLists = []

            # jump 2 idx since we check consecutive
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None

                mergedLists.append(self.utilsMerge(l1, l2))

            lists = mergedLists

        return lists[0]

    def utilsMerge(self, l1, l2):
        dummy = ListNode()
        curr = dummy

        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2

        return dummy.next
