class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

# 1st iteration -> count
# 2nd modify
# TC = O(2N)
# SC = O(1)


def brute_force(head):
    if not head:
        return None

    curr = head
    cnt0, cnt1, cnt2 = 0, 0, 0

    while curr:
        if curr.val == 0:
            cnt0 += 1
        elif curr.val == 1:
            cnt1 += 1
        elif curr.val == 2:
            cnt2 += 1
        curr = curr.next  # Move to the next node

    # Update LL
    curr = head
    for _ in range(cnt0):
        curr.val = 0
        curr = curr.next

    for _ in range(cnt1):
        curr.val = 1
        curr = curr.next

    for _ in range(cnt2):
        curr.val = 2
        curr = curr.next

    return head


# one-pass solution
# rearrange links

'''

- create 3 dummies
- traverse and rearrange the links

a b c d e f g h i j k l m n o
1 2 0 1 0 2 0 1 0 1 0 2 1 0 2 

                                    zero
dummyZero -> c -> e -> g -> i -> k -> n
                                one
dummyOne -> a -> d -> h -> j -> m
                            two
dummyTwo -> b -> f -> l -> o

- head = dummyZero.next
- zero.next = dummyOne.next
- one.next = dummyTwo.next

'''

def optimal(head):
    if not head or not head.next:
        return head
    
    zeroHead = Node(-1)
    oneHead = Node(-1)
    twoHead = Node(-1)
    
    zero = zeroHead
    one = oneHead
    two = twoHead
    
    curr = head
    
    # generate 3 lists
    while curr:
        if curr.val == 0:
            zero.next = curr
            zero = curr
        elif curr.val == 1:
            one.next = curr
            one = curr
        elif curr.val == 2:
            two.next = curr
            two = curr
        # increment curr
        curr = curr.next
    
    # merging 3 lists
    # connect end of zero to oneHead.next
    # if not exist then twoHead.next
    # if twoHead not exist then its by default None 
    zero.next = oneHead.next if oneHead.next else twoHead.next
    one.next = twoHead.next
    two.next = None
    
    newHead = zeroHead.next
    
    del zeroHead, oneHead, twoHead
    
    return newHead    