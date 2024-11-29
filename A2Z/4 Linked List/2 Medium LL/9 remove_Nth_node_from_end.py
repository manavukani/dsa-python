def removeNthFromEnd(head, n):
    left = head
    right = head

    while n > 0:
        right = right.next
        n -= 1
    
    if right is None:
        return head.next

    while right.next:
        left = left.next
        right = right.next

    # delete
    left.next = left.next.next
    return head
