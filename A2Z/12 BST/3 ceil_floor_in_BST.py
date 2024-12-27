class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# smallest value >= key
def ceil(root, key):
    if not root:
        return -1
    ceil_val = -1
    while root:
        if root.val == key:
            return root.val
        elif root.val < key:
            root = root.right
        # imp step - we want to find the smallest value >= key
        else:
            ceil_val = root.val
            root = root.left

    return ceil_val


# greatest value <= key
def floor(root, key):
    if not root:
        return -1

    floor_val = -1

    while root:
        if root.val == key:
            return root.val
        elif root.val > key:
            root = root.left
        else:
            floor_val = root.val
            root = root.right

    return floor_val


root = TreeNode(8)
root.left = TreeNode(4)
root.right = TreeNode(12)
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)
root.right.left = TreeNode(10)
root.right.right = TreeNode(14)

print("Ceil of 5:", ceil(root, 5))  # Output: 6
print("Floor of 5:", floor(root, 5))  # Output: 4
