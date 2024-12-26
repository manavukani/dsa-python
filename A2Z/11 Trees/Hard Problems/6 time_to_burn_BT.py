# from ANY given node

# time to burn a given node starting from src = distance of it from src
# time to burn a tree = max time to burn any node in the tree = max distance of any node from src

# TODO: find farthest node from src (using BFS)

from collections import deque


def solve(root, src):

    # node -> parent
    parent_mpp = {}

    def mark_parents(root, parent_mpp):
        q = deque([root])
        while q:
            curr = q.popleft()
            if curr.left:
                parent_mpp[curr.left] = curr
                q.append(curr.left)
            if curr.right:
                parent_mpp[curr.right] = curr
                q.append(curr.right)

    mark_parents(root, parent_mpp)

    # BFS to find farthest node from src
    visited = set()
    q = deque([(src, 0)])  # Store (node, distance) in the queue
    max_dist = 0

    while q:
        curr, dist = q.popleft()
        visited.add(curr)
        max_dist = max(max_dist, dist)

        # check left for next level
        if curr.left and curr.left not in visited:
            q.append((curr.left, dist + 1))
        # right
        if curr.right and curr.right not in visited:
            q.append((curr.right, dist + 1))
        # parent
        if parent_mpp.get(curr) and parent_mpp[curr] not in visited:
            q.append((parent_mpp[curr], dist + 1))

    return max_dist  # time to burn the tree


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
root.right.left = Node(0)
root.right.right = Node(8)

print(solve(root, root))
print(solve(root, root.right))
print(solve(root, root.left.right.left))


"""
IF NODE VALUE IS GIVEN INSTEAD OF NODE OBJECT --- NEED TO DO BFS TO FIND NODE OBJECT
"""


def burn_tree(root, src_data):
    # Find the source node and build parent-child mapping in "ONE PASS"
    parent_mpp = {}
    q = deque([(root, None)])  # Store (node, parent) in the queue
    src = None

    while q:
        curr, parent = q.popleft()

        if curr.data == src_data:
            src = curr

        if parent:
            parent_mpp[curr] = parent

        if curr.left:
            q.append((curr.left, curr))
        if curr.right:
            q.append((curr.right, curr))

    if src is None:
        return -1

    # BFS to find the farthest node from src
    visited = set()
    q = deque([(src, 0)])  # Store (node, distance) in the queue
    max_dist = 0

    while q:
        curr, dist = q.popleft()
        visited.add(curr)
        max_dist = max(max_dist, dist)

        if curr.left and curr.left not in visited:
            q.append((curr.left, dist + 1))
        if curr.right and curr.right not in visited:
            q.append((curr.right, dist + 1))
        if parent_mpp.get(curr) and parent_mpp[curr] not in visited:
            q.append((parent_mpp[curr], dist + 1))

    return max_dist
