class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

# brute -> traverse once to find length and then traverse again to delete

# optimal -> tortoise and hare method
def delete_middle_node(head):
    # single node -> delete it
    if not head or not head.next:
        return None

    slow = head
    
    # to stop before slow reaches middle
    # we skip 1 step for slow
    # so fast = head.next.next and slow is still at head
    if head.next:
        fast = head.next.next
    else:
        fast = None
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # slow.next is at middle
    slow.next = slow.next.next
    return head
