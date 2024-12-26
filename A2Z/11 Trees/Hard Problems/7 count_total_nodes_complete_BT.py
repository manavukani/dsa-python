# for a perfect tree - total nodes = 2^n - 1

# check left and right child of root, if they are equal height, then it is a perfect tree
# if not, total nodes = 1 + count_nodes(left) + count_nodes(right)

# Time complexity: less then O(n) as we are not traversing all nodes

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_nodes(root):
    if not root:
        return 0

    # Check if the tree is perfect
    lh = findHeightLeft(root)
    rh = findHeightRight(root)
    if lh == rh:
        return 2**lh - 1

    # If not perfect, count nodes recursively
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def findHeightLeft(node):
    hght = 0
    while node:
        hght += 1
        node = node.left
    return hght


def findHeightRight(node):
    # if not node:
    #     return 0
    # return 1 + findHeightRight(node.right)
    hght = 0
    while node:
        hght += 1
        node = node.right
    return hght


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

print("Height:", count_nodes(root))
