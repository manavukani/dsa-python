# given a 'SORTED DLL' and a sum 'k'
# find pairs which sum up to 'k'
# return all the pairs


class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


# TC < O(N^2)
# SC = O(1)
def brute(head, k):
    if not head or not head.next:  # If the list has fewer than 2 nodes
        return []

    res = set()
    temp = head
    while temp:
        req = k - temp.val
        curr = temp.next
        # since DLL is sorted -> we stop if val > req
        while curr and curr.val <= req:
            if curr.val == req:
                res.add((temp.val, curr.val))
            curr = curr.next
        temp = temp.next

    return list(res)

# OPTIMAL -----> two pointer approach -> Two Sum II
# TC = O(2N) -----> N for r and N for finding res
# SC = O(1)
def optimal(head, k):
    if not head or not head.next:  # If the list has fewer than 2 nodes
        return []

    res = set()
    l = head
    r = head

    # Move r to the last node
    while r.next:
        r = r.next

    # can use while l.val < r.val:
    # BUT THIS IS BETTER
    while l and r and l != r and l.prev != r:
        curr_sum = l.val + r.val
        if curr_sum == k:
            res.add((l.val, r.val))
            l = l.next
            r = r.prev
        elif curr_sum < k:
            l = l.next  # Move the left pointer forward
        else:
            r = r.prev  # Move the right pointer backward

    return list(res)


# Helper function to print the list
def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" <-> ")
        curr = curr.next
    print("None")

head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

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

# Find pairs with sum 6
pairs = optimal(head, 6)
print("Pairs with sum 6:")
print(pairs)
