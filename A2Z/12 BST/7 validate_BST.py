class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# neetcode approach
class Solution:
    def valid(self, node, left, right):
        if not node:
            return True
        if not (node.val < right and node.val > left):
            return False

        return self.valid(node.left, left, node.val) and self.valid(
            node.right, node.val, right
        )

    def isValidBST(self, root):

        return self.valid(root, float("-inf"), float("inf"))
