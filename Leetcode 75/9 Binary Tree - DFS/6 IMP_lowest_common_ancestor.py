class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, n1, n2):
        if not root or root == n1 or root == n2:
            return root
    
        left = self.lowestCommonAncestor(root.left, n1, n2)
        right = self.lowestCommonAncestor(root.right, n1, n2)
        
        if not left:
            return right
        elif not right:
            return left
        else:
            return root