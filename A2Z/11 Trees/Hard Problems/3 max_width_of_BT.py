# distance between two nodes in a binary tree, at the same level (lowest level with two nodes - not necessarily the lowest level of the tree)

#    1
#   / \
#  2   3
# / \   \
# 4  5   8
# max width = 4

#      1
#     / \
#    2   3
#   /     \
#   4      7
#  /        \
#  8         15
# max width = 8

# max width = last idx - first idx + 1 (at each level)
# use level order traversal


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


"""
challenge: assign correct index to each node

parent = i
left child = 2i+1 (0 based index)
right child = 2i+2 (0 based index)

but may cause overflow (if tree is very large or skewed) 
so subtract min value on that level from each index and use same formula (2i+1, 2i+2)

again, width = last index - first index + 1

"""

# time complexity: O(n)
# space complexity: O(n)
def max_width(root):
    if not root:
        return 0

    ans = 0
    from collections import deque

    q = deque()
    q.append((root, 0))

    while q:
        size = len(q)
        mmin = q[-1][1]  # first index / top element in queue
        for i in range(size):
            curr, idx = q.popleft()
            if i == 0:
                first = idx
            if i == size - 1:
                last = idx
            if curr.left:
                q.append((curr.left, 2 * idx + 1))
            if curr.right:
                q.append((curr.right, 2 * idx + 2))
        # update maximum width
        ans = max(ans, last - first + 1)

    return ans


root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.right.left = Node(0)
root.right.right = Node(8)
root.left.right.left = Node(7)
root.left.right.right = Node(4)

maxWidth = max_width(root)

print(f"Maximum width of the binary tree is: {maxWidth}")
