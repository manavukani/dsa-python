# brute
# traverse whole and find count
# find element at count//2
def find_middle(head):
    if head is None or head.next is None:
        return head
    temp = head
    count = 0
    while temp is not None:
        count += 1
        temp = temp.next
    mid = count // 2 + 1
    temp = head
    while temp is not None:
        mid = mid - 1
        if mid == 0:
            break
        temp = temp.next
    return temp

# ============ Tortoise and Hare Algorithm ============
# use slow and fast pointers

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def middle_element(head):
    if head is None or head.next is None:
        return head
    
    slow = head
    fast = head

    # for odd - fast.next ensures fast pointer doesn't go past the end of the list
    # fast at last node, and fast.next at null, signalling the end of the traversal.
    while fast and fast.next and slow:
        fast = fast.next.next
        slow = slow.next

    return slow

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
# head.next.next.next.next.next = Node(6)

print(middle_element(head))
