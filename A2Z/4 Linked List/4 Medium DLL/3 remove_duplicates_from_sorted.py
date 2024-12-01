# INPUT: 1 <-> 1 <-> 1 <-> 2 <-> 3 <-> 3 <-> 4
# DELETE =>    *     *                 *

# OUTPUT: 1 <-> 2 <-> 3 <-> 4

class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

# TC = O(N) ----> outer loop goes to non-duplicates (x) and inner loop goes to duplicates (N-x) -> overall N
# SC = O(1)
def solve(head):
    temp = head
    while temp and temp.next:
        if temp.val == temp.next.val:
            nextNode = temp.next
            # !! EDGE CASE !! - check if nextNode is not None
            while nextNode and temp.val == nextNode.val:
                nextNode = nextNode.next
            
            # deleting middle nodes
            temp.next = nextNode
            if nextNode: # if not @end (None)
                nextNode.prev = temp
        else:
            temp = temp.next
    return head

# Helper function to print the list
def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" <-> ")
        curr = curr.next
    print("None")

# Creating a sorted doubly linked list: 1 <-> 1 <-> 1 <-> 2 <-> 3 <-> 3 <-> 4
head = Node(1)
node2 = Node(1)
node3 = Node(1)
node4 = Node(2)
node5 = Node(3)
node6 = Node(3)
node7 = Node(4)

head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
node4.next = node5
node5.prev = node4
node5.next = node6
node6.prev = node5
node6.next = node7
node7.prev = node6

print("Original List:")
print_list(head)

# Remove duplicates
head = solve(head)
print("List After Removing Duplicates:")
print_list(head)