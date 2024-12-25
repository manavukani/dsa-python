#     1
#    / \
#   2   3
#  / \ / \
# 4  5,6  7
#    / \
#   8   9

# OUTPUT: 4 8 6 9 7
# 2 behind 8 and 5 behind 6

"""
same as top view, but we need to print the last element of each vertical line

but but but taking the last element in the list fails because the last node appended isn't
guaranteed to be the bottommost node - it depends on the depth of the tree.


- Store Depth in verticles:
    Each entry in verticles is (depth, value).
    The value is updated only if the current node is at a greater or equal depth for the same vertical line.
- Update Queue:
    Added depth as part of the tuple when nodes are enqueued.
- Output Values:
    Sorted by vertical position (v) and extracted only the values for the bottom view.
    
"""
from collections import defaultdict, deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bottom_view(root):
    if not root:
        return []

    q = deque([(root, 0, 0)])  # (node, vertical_level, depth)
    verticles = defaultdict(list)

    while q:
        curr, v, d = q.popleft()
        verticles[v].append((d, curr.val))  # Store (depth, value)

        if curr.left:
            q.append((curr.left, v - 1, d + 1))
        if curr.right:
            q.append((curr.right, v + 1, d + 1))

    res = []
    for v in sorted(verticles):
        # Find the node with the maximum depth at this vertical level
        max_depth = -1
        bottom_node = None
        for depth, val in verticles[v]:
            if depth >= max_depth:
                max_depth = depth
                bottom_node = val
        res.append(bottom_node)

    return res


"""
overwrites the node for a vertical position as soon as a new node is encountered in BFS level traversal

#    1
#   / \
#  2   3
#   \
#    4
#     \
#      5

"""


def striver(root):
    if not root:
        return []
    verticles = {}
    q = deque([(root, 0)])

    while q:
        curr, v = q.popleft()
        verticles[v] = curr.val
        if curr.left:
            q.append((curr.left, v - 1))
        if curr.right:
            q.append((curr.right, v + 1))

    # sort by vertical posn
    res = [verticles[v] for v in sorted(verticles.keys())]
    return res


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)
# root.left.right.left = Node(8)
# root.left.right.right = Node(9)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)


bottomView = bottom_view(root)
print(bottomView)  # 4 8 6 9 7
