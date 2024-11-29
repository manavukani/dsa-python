class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

# brute force - SC = O(N)


def brute(head):
    arr = []
    curr = head
    while curr:
        arr.append(curr.val)
        curr = curr.next

    arr.sort()

    curr = head
    i = 0
    while curr:
        curr.val = arr[i]
        i += 1
        curr = curr.next

    return head


# OPTIMAL => MERGE SORT
# TC = O(n logn)
# SC = O(1)
def sortList(head):
    def findMiddle(head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge_sorted_list(first, second):
        dummy = Node(0)
        curr = dummy

        while first and second:
            if first.val < second.val:
                curr.next = first
                first = first.next
            else:
                curr.next = second
                second = second.next
            curr = curr.next

        if first:
            curr.next = first
        if second:
            curr.next = second

        return dummy.next
    
    # Base case
    if not head or not head.next:
        return head

    middle = findMiddle(head)

    # Split into two
    right = middle.next
    middle.next = None
    left = head

    # sorting recursively 
    left = sortList(left)
    right = sortList(right)

    return merge_sorted_list(left, right)
