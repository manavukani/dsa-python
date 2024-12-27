class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# recursive
def insert(root, key):
    if not root:
        return TreeNode(key)

    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


# iterative
def insert(root, key):
    if not root:
        return TreeNode(key)

    curr = root
    while curr:
        if key < curr.val:
            if curr.left:
                curr = curr.left
            else:
                curr.left = TreeNode(key)
                break
        else:
            if curr.right:
                curr = curr.right
            else:
                curr.right = TreeNode(key)
                break
    return root


root = TreeNode(15)
root.left = TreeNode(10)
root.right = TreeNode(20)
root.left.left = TreeNode(8)
root.left.right = TreeNode(12)
root.right.left = TreeNode(17)
root.right.right = TreeNode(25)

insert(root, 13)

#         15
#        /  \
#      10    20
#     / \    / \
#    8  12  17  25
#        \
#         13

print(root.left.right.right.val)  # Output: 13
