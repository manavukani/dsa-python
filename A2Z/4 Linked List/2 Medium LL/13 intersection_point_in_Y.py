class Node:
    def __init__(self, val, next):
        self.next = next
        self.val = val

# brute -> traverse first, build hashmap (node, int), traverse 2nd and when find same. return that
# TC = O(M)+O(N)
# SC = O(M)+O(N)


def brute_force(list1, list2):
    curr = list1
    map1 = {}
    while curr:
        if curr not in map1:
            map1[curr] = curr.val
            curr = curr.next

    curr = list2
    while curr:
        if curr in map1:
            return curr
        else:
            curr = curr.next

    return None


# Space optimized
'''
- Find the length of both lists.
- Find the positive difference between these lengths.
- Move the dummy pointer of the larger list by the difference => search length reduced to a smaller list length.
- Move both pointers, each pointing two lists, ahead simultaneously if both do not collide.
'''

# TC = O(M+N)
# SC = O(1)


def space_optimized(list1, list2):
    def find_length(head):
        cnt = 0
        curr = head
        while curr:
            cnt += 1
            curr = curr.next
        return cnt

    len1 = find_length(list1)
    len2 = find_length(list2)
    curr1 = list1
    curr2 = list2

    if len1 > len2:
        while len1 > len2:
            curr1 = curr1.next
            len1 -= 1
    elif len1 < len2:
        while len1 < len2:
            curr2 = curr2.next
            len2 -= 1
    # both each now
    while curr1 and curr2:
        if curr1 == curr2:
            return curr1
        curr1 = curr1.next
        curr2 = curr2.next

    return None


# optimal -> optimize the length calculation by just finding the diff and moving that much
# TC - slightly better
# SC = O(1)
def optimal(head1, head2):
    def getDifference(head1, head2):
        len1 = 0
        len2 = 0
        # simultaneously traverse list1 and list2
        while head1 or head2:
            if head1:
                len1 += 1
                head1 = head1.next
            if head2:
                len2 += 1
                head2 = head2.next
        return len1 - len2

    diff = getDifference(head1, head2)

    # Advance the pointer of the longer list by the difference
    if diff < 0:
        while diff != 0:
            head2 = head2.next
            diff += 1
    else:
        while diff != 0:
            head1 = head1.next
            diff -= 1

    while head1:
        if head1 == head2:
            return head1  # Intersection point
        head1 = head1.next
        head2 = head2.next

    return None  # No intersection
