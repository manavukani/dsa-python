# TC = O(height) ----> best = log N, worst = N
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# iterative
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root is not None and root.val != val:
            root = root.left if val < root.val else root.right
        return root

# recursive
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        
        if root.val == val:
            return root

        if root.val > val:
           return self.searchBST(root.left, val)
        else:
           return self.searchBST(root.right, val)