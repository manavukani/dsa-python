# https://www.youtube.com/watch?v=ykelywHJWLg

"""
INPUT:

LL where every node represents a sub-linked-list and contains two pointers:
- next pointer to the next node
- bottom pointer to a linked list where this node is head

!!! IMP !!!
- Each of the sub-linked lists is in sorted order.

TODO: Flatten the Link List so all the nodes appear in a single level while maintaining the sorted order.

OUTPUT: traverse through bottom
"""


class Node:
    def __init__(self, x=0, nextNode=None, childNode=None):
        self.data = x
        self.next = nextNode
        self.child = childNode


"""

================ BRUTE FORCE ================

TC = O(N*M) + O(N*M log(N*M)) + O(N*M) ------> N = length along next, M = length along child
    traverse      sorting    utility func

SC = O(N*M) + O(N*M)   -----------> additional arry + result LL

"""


def brute_force(head):
    # utility func
    def convertArrToLinkedList(arr):
        dummyNode = Node(-1)
        curr = dummyNode
        for val in arr:
            curr.child = Node(val)
            curr = curr.child
        return dummyNode.child

    arr = []
    curr = head
    while curr:
        t2 = curr
        while t2:
            arr.append(t2.data)
            t2 = t2.child
        curr = curr.next
    arr.sort()
    return convertArrToLinkedList(arr)


"""
================ OPTIMAL ================


TC = O(N*M) + O(N*M log(N*M)) + O(N*M) ------> N = length along next, M = length along child
    traverse      sorting    utility func

SC = O(N*M) + O(N*M)   -----------> additional arry + result LL

"""

def optimal(head):
    def merge_sorted_LL(list1, list2):
        dummyNode = Node(-1)
        res = dummyNode

        while list1 and list2:
            if list1.data < list2.data:
                res.child = list1
                res = list1
                list1 = list1.child
            else:
                res.child = list2
                res = list2
                list2 = list2.child
            res.next = None
        if list1:
            res.child = list1
        else:
            res.child = list2
        if dummyNode.child:
            dummyNode.child.next = None
        return dummyNode.child

    # main logic
    if not head or not head.next:
        return head
    mergedHead = optimal(head.next)
    head = merge_sorted_LL(head, mergedHead)
    return head


### ======== UTILITIES FOR TESTING ======== 
def printLinkedList(head):
    while head:
        print(head.data, end=" ")
        head = head.child
    print()


def printOriginalLinkedList(head, depth):
    while head:
        print(head.data, end="")
        if head.child:
            print(" -> ", end="")
            printOriginalLinkedList(head.child, depth + 1)
        if head.next:
            print()
            print("| " * depth, end="")
        head = head.next

head = Node(5)
head.child = Node(14)
head.next = Node(10)
head.next.child = Node(4)
head.next.next = Node(12)
head.next.next.child = Node(20)
head.next.next.child.child = Node(13)
head.next.next.next = Node(7)
head.next.next.next.child = Node(17)

# Print the original
# linked list structure
print("Original linked list:")
printOriginalLinkedList(head, 0)

# Flatten the linked list
# and print the flattened list
flattened = optimal(head)
print("\nFlattened linked list: ", end="")
printLinkedList(flattened)
