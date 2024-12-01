class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
eg1:
Input: head = [1,2,3,4,5,6], k = 3
Output: [3,2,1,6,5,4]

eg2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]


"""


def _reverse(head):
    prevNode = None
    curr = head
    while curr is not None:
        nextNode = curr.next
        curr.next = prevNode
        prevNode = curr
        curr = nextNode
    return prevNode


# https://www.youtube.com/watch?v=lIar1skcQYI
# temp to kth node ------> break if k nodes not available
# store next and set next as None
# call reverse
# now head is newHead
# update head to kth node (back to beginning)
# temp is at end of reversed group, store it as prevNode
# take temp to stored next
# repeat steps and then connect prevNode to newHead


def findKthNode(head, k):
    k -= 1
    while head and k > 0:
        k -= 1
        head = head.next
    return head

# TC = O(2N) ---> N for traversing + N for finding Kth node
# SC = O(1)
def solve(head, k):
    temp = head
    nextGrpFirst = None
    prevGrpLast = None
    while temp:
        k_th_node = findKthNode(temp, k)
        if not k_th_node:
            # if not sufficient nodes
            if prevGrpLast:  # EDGE CASE, might not have k
                prevGrpLast.next = temp
            break

        # store next
        nextGrpFirst = k_th_node.next
        # separate group from rest list
        k_th_node.next = None

        _reverse(temp)
        # for the first group ---> need to update the head
        if temp == head:
            # newHead
            head = k_th_node
        # for rest of the groups
        else:
            prevGrpLast.next = k_th_node

        # store temp, move to next
        prevGrpLast = temp
        temp = nextGrpFirst
    
    return head
