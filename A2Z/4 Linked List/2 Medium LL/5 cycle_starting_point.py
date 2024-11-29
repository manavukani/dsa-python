class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# BRUTE => same as cycle detection, but instead return curr node
# TC: O(N), SC: O(N)
def detect_loop(head):
    temp = head
    node_map = {}
    while temp is not None:
        if temp in node_map:
            return temp
        # store temp as visited
        node_map[temp] = True
        temp = temp.next
    return None

# SLOW AND FAST POINTER ===== TORTOISE AND HARE
# TC: O(N), SC: O(1)
def optimal(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    # if no loop
    return None


node1 = Node(1)
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3
node4 = Node(4)
node3.next = node4
node5 = Node(5)
node4.next = node5

# Make a loop from node5 to node2
node5.next = node2

# Set the head of the linked list
head = node1

# Detect the loop in the linked list
loop_start_node = optimal(head)

if loop_start_node:
    print("Loop detected. Starting node of the loop is:", loop_start_node.data)
else:
    print("No loop detected in the linked list.")


'''
In the "tortoise and hare" algorithm
- slow pointer reaches starting point of loop, fast pointer is positioned at twice the distance travelled by slow pointer (moves at double the speed)
- Now slow and fast entered the loop, distance fast cover to catch up to slow is the total length of loop minus L1. Let this distance be d.

=> Distance travelled by slow = L1
=> Distance travelled by fast = 2 * L1
=> Total length of loop = L1 + d

- Fast pointer advances toward the slow pointer with two jumps per step, while the slow pointer moves away with one jump per step.
- The gap between them decreases by 1 with each step. 
- Given that the initial gap is d, it takes exactly d steps for them to meet.

=> Total length of loop = L1 + d
=> Distance between slow and fast= d

- During these d steps, the slow pointer effectively travels d steps from the starting point within the loop and fast travels 2 x d and they meet a specific point. 

- Based on our previous calculations, the total length of the loop is L1 + d. And since the distance covered by the slow pointer within the loop is d, the remaining distance within the loop is equal to L1.

- Therefore, it is proven that the distance between the starting point of the loop and the point where the two pointers meet is indeed equal to the distance between the starting point and head of the linked list.
'''