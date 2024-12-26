# Given a BT and a root.
# Return the path from the root node to the given leaf node.
# IMP CONDITIONS:
# 1. No two nodes in the tree have the same data value.
# 2. It is assured that the given node is present and a path always exists.


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def get_path(root, node, arr, target):
    if not root:
        return False

    # add the current node to the path
    arr.append(root.data)

    # check if curr is target
    if root.data == node:
        return True

    # if any of them has the target, return True
    if get_path(root.left, node, arr, target) or get_path(
        root.right, node, arr, target
    ):
        return True

    # if not found target, remove the curr node from the path array (backtrack to the previous node)
    arr.pop()

    return False


def root_to_node_path(root, node):
    arr = []
    if not root:
        return arr
    get_path(root, node, arr, node)

    return arr


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(root_to_node_path(root, 5))  # [1, 2, 5]
print(root_to_node_path(root, 7))  # [1, 3, 7]
