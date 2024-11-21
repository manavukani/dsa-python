class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

def printDLL(head):
    curr = head
    while curr is not None:
        print(curr.data, end=' <--> ')
        curr = curr.next
    print()

def convert_arr_to_dll(arr):
    # Create the head node with the first element of the array
    head = Node(arr[0])
    # Initialize 'prev' to the head node
    prev = head

    for i in range(1, len(arr)):
        # Create a new node with data from the array and set its 'back' pointer to the previous node
        temp = Node(arr[i], None, prev)
        
        # Update the 'next' pointer of the previous node to point to the new node
        prev.next = temp
        # Move 'prev' to the newly created node for the next iteration
        prev = temp

    # Return the head of the doubly linked list
    return head

# Time = O(2N)
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

# Both space and time = O(N)
def better_recursive(curr):
    # Base case: list is empty or we reach the end of the list
    if curr is None:
        return None

    # Swap the next and prev pointers
    temp = curr.prev
    curr.prev = curr.next
    curr.next = temp

    # If the previous node (after swap) is null, this is the new head
    if curr.prev is None:
        return curr

    # Recurse for the next node
    return better_recursive(curr.prev)

# Time = O(N), Space = O(1)
'''
Initially, prevNode is set to NULL and currNode starts at the head.
As the list is traversed,
- Update prevNode to currNode's prev, prevNode = currNode->prev.
- Update currNode's prev pointer to its next node, currNode->prev = currNode->next.
- Update currNode's next pointer to prevNode, currNode->next = prevNode.
- Move currNode to the next node, currNode = currNode->prev.
After traversing all the nodes, prevNode will point to the second node of the reversed list, so update the previous pointer of prevNode as the new head of the linked list, head = prevNode->prev and return it.

'''
def optimal(head):
    if head is None or head.next is None:
        return head
    
    prevNode = None
    currNode = head
    
    while currNode is not None:
        # Swap the next and prev pointers
        prevNode = currNode.prev
        currNode.prev = currNode.next
        currNode.next = prevNode
        
        # Move to the next node in the original list
        # (which is now previous due to reversal)
        currNode = currNode.prev
        
    # The final node in the original list
    # becomes the new head after reversal
    return prevNode.prev
        


if __name__ == "__main__":

    arr = [1,2,3,4,5,6,7]
    head = convert_arr_to_dll(arr)
    printDLL(head)
    
    # rev = brute(head)
    # rev = better_recursive(head)
    rev = optimal(head)
    printDLL(rev)
