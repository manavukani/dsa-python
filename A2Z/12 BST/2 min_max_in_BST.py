class TreeNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


class Solution:
    def minValue(self, root):
        if not root:
            return None
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr.data

    def maxValue(self, root):
        if not root:
            return None
        curr = root
        while curr and curr.right:
            curr = curr.right
        return curr.data


#         15
#        /  \
#      10    20
#     / \    / \
#    8  12  17  25


# Creating the BST
root = TreeNode(15)
root.left = TreeNode(10)
root.right = TreeNode(20)
root.left.left = TreeNode(8)
root.left.right = TreeNode(12)
root.right.left = TreeNode(17)
root.right.right = TreeNode(25)

# Create a Solution object
sol = Solution()

# Find the minimum and maximum elements
print("Minimum value in BST:", sol.minValue(root))  # Output: 8
print("Maximum value in BST:", sol.maxValue(root))  # Output: 25
