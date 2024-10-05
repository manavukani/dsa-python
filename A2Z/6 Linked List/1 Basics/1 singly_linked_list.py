'''
Insertion:
- At the beginning: O(1)
- At the end: O(n)
- At a specific position: O(n)
Deletion:
- At the beginning: O(1)
- At the end: O(n)
- At a specific position: O(n)
Search: O(n)
Traversal: O(n)
'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def printLL(head):
    while head is not None:
        print(head.data, end="-->")
        head = head.next
    print()

# INSERTION


def insert_head(head, val):
    new_node = Node(val, head)
    return new_node


def insert_tail(head, val):
    if head is None:
        new_node = Node(val, head)
        return new_node

    temp = head
    # go till end
    while temp.next is not None:
        temp = temp.next
    # add new node
    new_node = Node(val)
    temp.next = new_node
    
    # free memory
    del temp
    return head


def insert_k(head, val, posn):
    if head is None:
        if posn == 1:
            # new_node = Node(val)
            return Node(val)
        else:
            raise Exception("Cannot insert at given posn in NULL linked list")

    # insert at head
    if posn == 1:
        # new_node = Node(val, head)
        return Node(val, head)

    # if posn >= 1
    count = 0
    temp = head
    while temp is not None:
        count += 1
        if count == posn - 1:
            # create the new node and new node next to current's next
            new_node = Node(val, temp.next)
            # new_node.next = temp.next
            # assign current node next to new node
            temp.next = new_node
            break
        temp = temp.next

    return head


'''CANNOT HANDLE INSERTION BEFORE HEAD'''
# def insert_before_x (head, val, x):
#     if head is None:
#         raise Exception("cannot insert before value in empty linked list")
#     # inserting before an element => no need to go till end
#     temp = head
#     while temp.next is not None:
#         if temp.next.data == x:
#             new_node = Node(val, temp.next)
#             temp.next = new_node
#             break
#         temp = temp.next
#     return head


def insert_before_x(head, val, x):
    if head is None:
        raise Exception("Cannot insert before value in empty linked list")

    # Handle insertion before the head
    if head.data == x:
        new_node = Node(val, head)
        return new_node  # New head

    temp = head
    while temp.next is not None:
        if temp.next.data == x:
            new_node = Node(val, temp.next)
            temp.next = new_node
            return head  # Return the original head after insertion
        temp = temp.next

    raise Exception(f"Value {x} not found in the linked list.")


def insert_after_x(head, val, x):
    if head is None:
        raise Exception("cannot insert before value in empty linked list")
    # need to traverse each node
    temp = head
    while temp is not None:
        if temp.data == x:
            new_node = Node(val, temp.next)
            temp.next = new_node
            break
        temp = temp.next
    return head

# DELETION


def delete_tail(head):
    if head is None or head.next is None:
        return None

    # head is important -> as we always return it for LC
    temp = head

    while temp.next.next is not None:
        temp = temp.next

    temp.next = None

    return head


def delete_head(head):
    if head is None:
        return head
    head = head.next
    return head


def delete_k(head, posn):
    # empty => default edge case for all LL
    if head == None:
        return None

    if posn == 1:
        head = head.next
        return head

    temp = head
    prev = None
    count = 0

    while temp is not None:

        count += 1
        if count == posn:
            prev.next = prev.next.next
            break

        prev = temp
        temp = temp.next

    return head


def delete_by_value(head, val):
    if head == None:
        return None

    temp = head
    prev = None

    while temp is not None:
        if temp.data == val:
            prev.next = prev.next.next
            break
        prev = temp
        temp = temp.next

    return head

# OTHERS


def length(head):
    temp = head
    count = 0
    while temp is not None:
        count += 1
        temp = temp.next
    return count


def search(head, target):

    temp = head

    while temp is not None:
        if temp.data == target:
            return True
        temp = temp.next

    return False


# def array_to_LL(data_list):
#     head = Node(None)
#     for data in data_list:
#         insert_head(head, data)
#     return head


if __name__ == "__main__":
    arr = [12, 8, 5, 7]
    # myLL = array_to_LL(arr)
    # printLL(myLL)

    # 12-->8-->5-->7-->
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])

    printLL(head)

    # Length
    print(length(head))

    # Search
    print(search(head, 5))
    print(search(head, 54))
    print(search(head, 8))

    # ============= INSERTING =============
    # at head
    head = insert_head(head, 100)
    printLL(head)

    # at tail
    head = insert_tail(head, 200)
    printLL(head)

    # at K th position
    head = insert_k(head, 300, 5)
    printLL(head)

    # before X value
    # cannot handle inserting before head =====> RESOLVED
    head = insert_before_x(head, 400, 100)
    printLL(head)

    head = insert_after_x(head, 600, 100)
    printLL(head)

    # ============= DELETING =============
    # head  => need to assign head to function!!!
    head = delete_head(head)
    printLL(head)

    # tail
    head = delete_tail(head)
    printLL(head)

    # K th element => normal indexing
    delete_k(head, 2)
    printLL(head)

    # by value of node
    delete_by_value(head, 5)
    printLL(head)

    delete_by_value(head, 8)
    printLL(head)
