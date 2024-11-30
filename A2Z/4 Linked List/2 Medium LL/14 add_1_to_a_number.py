class Node:
    def __init__(self, val, next):
        self.next = next
        self.val = val

# TC = O(3N) ---> reverse + traverse + reverse
# SC = O(1)
def brute(head):
    def reverse_LL(head):
        curr = head
        prevNode = None
        while curr:
            nextNode = curr.next
            curr.next = prevNode
            prevNode = curr
            curr = nextNode
        return prevNode
    head = reverse_LL(head)

    curr = head
    carry = 1  # we add 1

    while curr:
        curr.val = curr.val + carry
        if curr.val < 10:
            carry = 0
            break
        else:
            curr.val = 0
            carry = 1
        curr = curr.val

    # 2 cases: we break or completion done
    # if carry exists at end
    if carry == 1:
        newNode = Node(1)
        head = reverse_LL(head)
        newNode.next = head
        return newNode
    # if not carry
    else:
        head = reverse_LL(head)
        return head

# without reversing --- need to use recursion (backtracking)
# TC = O(N)
# SC = O(N) -> Recursive Stack Space
def optimal(head):
    def helper(head):
        # base case
        if head == None:
            return 1

        carry = helper(head.next)
        head.val = head.val + carry
        if head.val < 10:
            return 0
        head.val = 0
        return 1

    carry = helper(head)
    if carry == 1:
        newNode = Node(1)
        newNode.next = head
        return newNode

    return head
