# given a doubly linked list and a key
# delete all the occurrences
# return the new head

class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

# TC = O(N)

# !!! EDGE CASES !!!
# - when node is head, there is no prev
# - when node is tail, there is no next

def delete_all_occurrence(head, key):
    curr = head
    while curr:
        if curr.val == key:
            if curr == head:
                head = head.next
            nextNode = curr.next
            prevNode = curr.prev
            
            if nextNode:
                nextNode.prev = prevNode
            if prevNode:
                prevNode.next = nextNode
            curr = nextNode  # Move to the next node
        # not equal to key
        else:
            curr = curr.next
    return head

# Helper function to print the list
def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" <-> ")
        curr = curr.next
    print("None")

# Creating a doubly linked list: 1 <-> 2 <-> 3 <-> 2 <-> 4
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(2)
node5 = Node(4)

head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
node4.next = node5
node5.prev = node4

print("Original List:")
print_list(head)

# Delete all occurrences of 2
head = delete_all_occurrence(head, 2)

print("After Deleting All Occurrences of 2:")
print_list(head)
