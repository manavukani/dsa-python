# In-place reversal, recursive and iterative approaches

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# ========== BRUTE - NEVER DO THIS ============> time = O(2N), space = O(N)
def brute(head):
    # If head is empty or there is only one element, return the head directly
    if head is None or head.next is None:
        return head
    # keep track of all elements ========= O(n)
    stack = []
    curr = head
    while curr is not None:
        stack.append(curr.data)
        curr = curr.next

    # pop and make a LL ========= O(n)
    curr = head
    while curr is not None:
        curr.data = stack.pop()
        curr = curr.next

    return head

# ========== ITERATIVE ============> TIME - O(N)
def reverse_iterative(head):
    prevNode = None
    curr = head
    while curr is not None:
        # store next node
        nextNode = curr.next
        # reverse the next
        curr.next = prevNode
        # increment prevNode
        prevNode = curr
        # increment current to next
        curr = nextNode
    # loop ended => current and nextNode reach null 
    return prevNode


def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end="-->")
        temp = temp.next
    print()

head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(4)

print("Original Linked List:", end=" ")
print_linked_list(head)

# head = brute(head)
head = reverse_iterative(head)

print("Reversed Linked List:", end=" ")
print_linked_list(head)