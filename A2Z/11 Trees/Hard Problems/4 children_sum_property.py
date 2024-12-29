# value of each node = sum of its children
# if no children, value of child = 0

# can only increment value of node


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# time complexity: O(n)
# use recusrion, go left, go right and then return
# if left + right < root -- assign them equal to root (so when we return we do not fall short, coz we cant decrease root)
# if left + right > root -- assign root equal to left + right (we can increase the root if required)
def reorder_tree(root):
    if not root:
        return

    child = 0
    if root.left:
        child += root.left.data
    if root.right:
        child += root.right.data

    # if child (sum) is greater, update root -- so that we do not fall short
    if child >= root.data:
        root.data = child
    # if child (sum) is less, update children
    else:
        if root.left:
            root.left.data = root.data
        elif root.right:
            root.right.data = root.data

    # go left and right recursively
    reorder_tree(root.left)
    reorder_tree(root.right)

    # come back and update the root with sum of children
    total = 0
    if root.left:
        total += root.left.data
    if root.right:
        total += root.right.data
    if root.left or root.right:
        root.data = total


def inorderTraversal(root):
    if root is None:
        return
    inorderTraversal(root.left)
    print(root.data, end=" ")
    inorderTraversal(root.right)


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)


print("Binary Tree before modification:", end=" ")
inorderTraversal(root)
print()

reorder_tree(root)

print("Binary Tree after Children Sum Property:", end=" ")
inorderTraversal(root)
print()
