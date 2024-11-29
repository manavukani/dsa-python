"----------------------- BASIC -----------------------"

def copyRandomList(head):
    mpp = {None:None}
    cur = head
    while cur:
        copy = Node(cur.val)
        mpp[cur] = copy
        cur = cur.next
    
    cur = head
    while cur:
        copy = mpp[cur]
        copy.next = mpp[cur.next]
        copy.random = mpp[cur.random]
        cur = cur.next
    
    return mpp[head]


"----------------------- OPTIMAL -----------------------"

# Node class to represent
# elements in the linked list
class Node:
    # Data stored in the node
    def __init__(self, x):
        self.data = x
        # Pointer to the next node
        self.next = None
        # Pointer to a random
        # node in the list
        self.random = None

# Function to insert a copy of each
# node in between the original nodes
def insertCopyInBetween(head):
    temp = head
    while temp:
        nextElement = temp.next
        # Create a new node with the same data
        copy = Node(temp.data)

        # Point the copy's next to
        # the original node's next
        copy.next = nextElement

        # Point the original
        # node's next to the copy
        temp.next = copy

        # Move to the next original node
        temp = nextElement

# Function to connect random
# pointers of the copied nodes
def connectRandomPointers(head):
    temp = head
    while temp:
        # Access the copied node
        copyNode = temp.next

        # If the original node
        # has a random pointer
        if temp.random:
            # Point the copied node's random to the
            # corresponding copied random node
            copyNode.random = temp.random.next
        else:
            # Set the copied node's random to
            # null if the original random is null
            copyNode.random = None

        # Move to the next original node
        temp = temp.next.next

# Function to retrieve the
# deep copy of the linked list
def getDeepCopyList(head):
    temp = head
    # Create a dummy node
    dummyNode = Node(-1)
    # Initialize a result pointer
    res = dummyNode

    while temp:
        # Creating a new List by
        # pointing to copied nodes
        res.next = temp.next
        res = res.next

        # Disconnect and revert back to the
        # initial state of the original linked list
        temp.next = temp.next.next
        temp = temp.next

    # Return the deep copy of the
    # list starting from the dummy node
    return dummyNode.next

# Function to clone the linked list
def cloneLL(head):
    # If the original list
    # is empty, return null
    if not head:
        return None

    # Step 1: Insert copy of
    # nodes in between
    insertCopyInBetween(head)
    # Step 2: Connect random
    # pointers of copied nodes
    connectRandomPointers(head)
    # Step 3: Retrieve the deep
    # copy of the linked list
    return getDeepCopyList(head)

# Function to print the cloned linked list
def printClonedLinkedList(head):
    while head:
        print("Data:", head.data, end="")
        if head.random:
            print(", Random:", head.random.data, end="")
        else:
            print(", Random: None", end="")
        print()
        # Move to the next node
        head = head.next

# Main function
if __name__ == "__main__":
    # Example linked list: 7 -> 14 -> 21 -> 28
    head = Node(7)
    head.next = Node(14)
    head.next.next = Node(21)
    head.next.next.next = Node(28)

    # Assigning random pointers
    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next.next.next
    head.next.next.next.random = head.next

    print("Original Linked List with Random Pointers:")
    printClonedLinkedList(head)

    # Clone the linked list
    clonedList = cloneLL(head)

    print("\nCloned Linked List with Random Pointers:")
    printClonedLinkedList(clonedList)

                                
                            