class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNode(head):
    
    if not head or head.next == None:
        return None
    
    slow = head
    fast = head.next.next if head.next else None
    
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next
    
    # slow will be at middle
    slow.next = slow.next.next
    return head