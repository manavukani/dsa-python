class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# brute -> using Stack
# TC = O(2N), SC = O(N)


def brute(head):
    temp = head
    stack = []
    while temp:
        stack.append(temp.val)
        temp = temp.next
    # checking
    l, r = 0, len(stack) - 1
    while l <= r:
        if stack[l] != stack[r]:
            return False
        l += 1
        r -= 1
    return True


# Space optimized

def optimal(head):
    def reverse_LL(head):
        curr = head
        prevNode = None
        while curr:
            nextNode = curr.next
            curr.next = prevNode
            prevNode = curr
            curr = nextNode
        return prevNode
    
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    newHead = reverse_LL(slow)
    
    first = head
    second = newHead
    
    # IMP - go till end of "second" and not first, check print
    # print_LL(first)
    # print_LL(second)
    while second:
        if first.val != second.val:
            reverse_LL(newHead) # make original before return
            return False
        first = first.next
        second = second.next

    reverse_LL(newHead) # make original before return
    return True


def print_LL(head):
    temp = head
    while temp is not None:
        print(temp.val, end="-->")
        temp = temp.next
    print()

head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(2)
head.next.next.next.next = Node(3)
head.next.next.next.next.next = Node(1)

print("Original Linked List:", end=" ")
print_LL(head)

print("IS PALINDROME:", optimal(head))