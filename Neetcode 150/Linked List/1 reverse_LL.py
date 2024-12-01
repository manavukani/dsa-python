# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        prevNode = None
        curr = head
        
        while curr:
            # store next node
            nextNode = curr.next
            # reverse the next
            curr.next = prevNode
            # increment prevNode
            prevNode = curr
            # increment current to next
            curr = nextNode
        return prevNode