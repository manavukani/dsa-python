# In-place reversal, recursive and iterative approaches

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# =================> TIME - O(N)
# =================> SPACE - O(N) {RECURSIVE STACK SPACE}
def reverse_recursive(head):
    # base case => just the head or null
    if head is None or head.next is None:
        return head
    
    newHead = reverse_recursive(head.next)
    nextNode = head.next
    nextNode.next = head
    head.next = None

    return newHead

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

head = reverse_recursive(head)

print("Reversed Linked List:", end=" ")
print_linked_list(head)