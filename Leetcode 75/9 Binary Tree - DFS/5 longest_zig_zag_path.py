class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TC = O(n)
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return max(self.helper(root.left, True, 0), self.helper(root.right, False, 0))

    def helper(self, root, isLeft, depth):
        if not root:
            return depth

        # previous direction = left
        if isLeft:
            depth = max(
                depth, # previous max
                self.helper(root.right, False, depth + 1), # zig-zag continue
                self.helper(root.left, True, 0), # reset
            )
        # previous = Right
        else:
            depth = max(
                depth, # previous max
                self.helper(root.left, True, depth + 1), # zig-zag continue
                self.helper(root.right, False, 0), # reset
            )

        return depth