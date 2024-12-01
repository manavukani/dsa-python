# same as rotate the array right but with LL

# TC = O(N)
# SC = O(1)
def rotateRight(head, k):
    if not head or not head.next or k == 0:
        return head

    # STEP 1:traverse and reach tail node
    temp = head
    n = 1
    while temp.next:
        temp = temp.next
        n += 1

    # STEP 2: make tail point to head
    # temp @ last
    temp.next = head

    # STEP 3: handling larger k
    k = k % n
    # multiples of k ----> return same LL
    if k == 0:
        temp.next = None
        return head

    # STEP 4: reach the "n-k-1" node
    curr = head
    count = n - k
    for _ in range(count - 1):
        curr = curr.next
    # curr @ n-k-1

    # STEP 5: adjusting the newHead and newTail
    newHead = curr.next
    curr.next = None  # new tail

    return newHead
