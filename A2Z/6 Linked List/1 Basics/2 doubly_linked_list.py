'''
Deletion Operations
- Deletion at the Beginning: O(1)
- Deletion after a given node: O(1)
- Deletion before a given node: O(1)
- Deletion at a specific position: O(n)
- Deletion at the End: O(n)
Insertion Operations
- Insertion at the Beginning: O(1)
- Insertion after a given node: O(1)
- Insertion before a given node: O(1)
- Insertion at a specific position: O(n)
- Insertion at the End: O(n)
'''

class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


def insert_head(head, val):
    new_node = Node(val)

    if head is None:
        return new_node

    new_node.next = head
    head.prev = new_node

    return new_node


def insert_tail(head, val):
    new_node = Node(val)

    if head is None:
        return new_node

    else:
        tail = head
        while tail.next is not None:
            tail = tail.next
        tail.next = new_node
        new_node.prev = tail

    return head


def insert_after_x(head, val, x):
    if head is None:
        raise Exception("cannot insert before value in empty linked list")
    else:
        # temp is current
        temp = head
        while temp is not None:
            if temp.data == x:
                new_node = Node(val)
                new_node.next = temp.next
                new_node.prev = temp
                # always change current's next to new node at last
                temp.next = new_node
                if new_node.next is not None:
                    new_node.next.prev = new_node
                break
            temp = temp.next

    # if not found, also returns head
    return head


''' =================== CANNOT HANDLE INSERTION BEFORE HEAD =================== '''


def old_insert_before_x(head, val, x):
    if head is None:
        raise Exception("cannot insert before value in empty linked list")
    else:
        temp = head
        while temp.next is not None:
            if temp.next.data == x:
                new_node = Node(val)
                new_node.next = temp.next
                new_node.prev = temp
                temp.next = new_node
                if new_node.next is not None:
                    new_node.next.prev = new_node
                break
            temp = temp.next

    return head


''' =================== RESOLVED ====================== '''


def insert_before_x(head, val, x):
    if head is None:
        raise Exception("Cannot insert before value in an empty linked list")

    temp = head

    # Search for the node containing x
    while temp is not None:
        if temp.data == x:
            break
        temp = temp.next

    # If x was not found, return the original head
    if temp is None:
        return head

    new_node = Node(val)

    # Inserting at the head
    if temp.prev is None:
        new_node.next = head
        head.prev = new_node
        head = new_node
    else:
        new_node.prev = temp.prev
        new_node.next = temp
        temp.prev.next = new_node
        temp.prev = new_node

    return head


def insert_k(head, val, posn):
    if head is None:
        if posn == 1:
            return Node(val)
        else:
            raise Exception("Cannot insert at given posn in NULL linked list")

    if posn == 1:
        new_node = Node(val)
        new_node.next = head
        head.prev = new_node
        return new_node

    # posn >= 1
    curr = head
    count = 0
    while curr is not None:
        count += 1
        if count == posn - 1:
            new_node = Node(val)
            new_node.next = curr.next
            new_node.prev = curr
            if new_node.next is not None:
                new_node.next.prev = new_node
            # ALWAYS LAST ==> assign current node's next to new node
            curr.next = new_node
            break
        curr = curr.next

    return head


''' =================== ALTERNATIVE WAY =================== '''


def insert_at_position(head, pos, new_data):
    # Create a new node
    new_node = Node(new_data)

    # Insertion at the beginning
    if pos == 1:
        new_node.next = head

        # If the linked list is not empty, set the prev of head to new node
        if head is not None:
            head.prev = new_node

        # Set the new node as the head of the linked list
        head = new_node
        return head

    curr = head

    # Traverse the list to find the node before the insertion point
    for _ in range(1, pos - 1):
        if curr is None:
            print("Position is out of bounds.")
            return head
        curr = curr.next

    # If the position is out of bounds
    if curr is None:
        print("Position is out of bounds.")
        return head

    # Set the prev of new node to curr
    new_node.prev = curr

    # Set the next of new node to next of curr
    new_node.next = curr.next

    # Update the next of current node to new node
    curr.next = new_node

    # If the new node is not the last node, update prev of next node to new node
    if new_node.next is not None:
        new_node.next.prev = new_node

    return head


def delete_head(head):
    if head is not None:
        head = head.next
        # new head's prev
        head.prev = None
    return head

def delete_tail(head):
    # if empty => None
    if head is None or head.next is None:
        return None
    # else traverse to end
    if head is not None:
        curr = head
        while curr.next is not None:
            curr = curr.next
        # curr is last
        curr.prev.next = None
        curr.next = None
    return head


# BASS HO GAYA
def delete_after(head, key):
    curr = head

    # Iterate over Linked List to find the key
    while curr is not None:
        if curr.data == key:
            break
        curr = curr.next

    # If curr is None or curr.next is None, 
    # there is no node to delete
    if curr is None or curr.next is None:
        return head

    # Node to be deleted
    node_delete = curr.next

    # Update the next of the current node to 
    # the next of the node to be deleted
    curr.next = node_delete.next

    # If the node to be deleted is not the last node,
    # update the previous pointer of the next node
    if node_delete.next is not None:
        node_delete.next.prev = curr

    return head

def delete_before(head, key):
    curr = head

    # Find the node with the given key
    while curr is not None:
        if curr.data == key:
            break
        curr = curr.next

    # If curr is None or curr.prev is None,
    # there is no node to delete
    if curr is None or curr.prev is None:
        return head

    # Node to be deleted
    nodeToDelete = curr.prev

    # Update the prev of the current node to the prev 
    # of the node to be deleted
    curr.prev = nodeToDelete.prev

    # If nodeToDelete's prev is not None, update its 
    # next pointer to the current node
    if nodeToDelete.prev is not None:
        nodeToDelete.prev.next = curr
    else:
        # If nodeToDelete is the head node
        head = curr

    return head


def del_pos(head, pos):
  
    # If the list is empty
    if head is None:
        return head

    curr = head

    # Traverse to the node at the given position
    for i in range(1, pos):
        if curr is None:
            return head
        curr = curr.next

    # If the position is out of range
    if curr is None:
        return head

    # Update the previous node's next pointer
    if curr.prev is not None:
        curr.prev.next = curr.next

    # Update the next node's prev pointer
    if curr.next is not None:
        curr.next.prev = curr.prev

    # If the node to be deleted is the head node
    if head == curr:
        head = curr.next

    # Return the updated head
    return head

def printLL(head):
    curr = head
    while curr is not None:
        print(curr.data, end=' <--> ')
        curr = curr.next
    print()


if __name__ == "__main__":

    # 2 <-> 3 <-> 4
    head = Node(2)
    head.next = Node(3)
    head.next.prev = head
    head.next.next = Node(4)
    head.next.next.prev = head.next
    printLL(head)

    head = insert_head(head, 100)
    printLL(head)

    head = insert_tail(head, 900)
    printLL(head)

    head = insert_after_x(head, 800, 900)
    printLL(head)

    head = insert_before_x(head, 600, 100)
    printLL(head)

    head = insert_k(head, 700, 1)
    printLL(head)
    
    head = delete_head(head)
    printLL(head)
    
    head = delete_tail(head)
    printLL(head)
    
    head = delete_after(head, 600)
    printLL(head)
    
    head = delete_before(head, 900)
    printLL(head)
    
    head = del_pos(head, 1)
    printLL(head)