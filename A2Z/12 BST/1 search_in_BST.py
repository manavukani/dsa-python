class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def searchBST(root, val):

    while root is not None and root.val != val:
        root = root.left if val < root.val else root.right
    return root


def printInOrder(root):
    if root is None:
        return
    printInOrder(root.left)
    print(root.val, end=" ")
    printInOrder(root.right)


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(10)

print("Binary Search Tree:")
printInOrder(root)
print()


# Searching for a value in the BST
target = 42232
print(True) if searchBST(root, target) else print(False)
