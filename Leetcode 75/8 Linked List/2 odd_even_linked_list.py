# naive with O(n) space -> build array to store odd first and then even idx (keep appending alternate posn)


# optimal - O(1) space
def oddeven(head):
    if not head or not head.next:
        return head

    odd = head
    even = head.next
    evenHead = head.next

    while even and even.next:
        odd.next = odd.next.next  # alternate
        even.next = even.next.next  # alternate

        # iterate
        odd = odd.next
        even = even.next

    # odd followed by even
    odd.next = evenHead

    return head
