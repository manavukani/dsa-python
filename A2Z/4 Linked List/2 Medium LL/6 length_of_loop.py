# no loop => return 0
# loop => return length of loop

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# TC = O(N), SC = O(N)
def brute_force(head):
    visited_nodes = {}
    temp = head
    timer = 0

    while temp is not None:
        # If the node is revisited, calculate and return the loop length
        if temp in visited_nodes:
            return timer - visited_nodes[temp]

        # Store the current node and its timer value
        visited_nodes[temp] = timer
        temp = temp.next
        timer += 1
    return 0


# optimal -> TC = O(n), SC = O(1)
def tortoise_hare(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # loop detected
        if slow == fast:
            count = 1
            slow = slow.next # IMP
            while fast != slow:
                count += 1
                slow = slow.next
            return count
    # NO LOOP
    return 0


head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = second  # Creates a loop

loop_length = tortoise_hare(head)

if loop_length > 0:
    print(f"Length of the loop: {loop_length}")
else:
    print("No loop found in the linked list.")
