class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, root, maxi):
        if root is None:
            return 0

        leftMax = max(0, self.helper(root.left, maxi))
        rightMax = max(0, self.helper(root.right, maxi))

        maxi[0] = max(maxi[0], leftMax + rightMax + root.val)

        return max(leftMax, rightMax) + root.val

    def maxPathSum(self, root) -> int:
        maxi = [float('-inf')]
        self.helper(root, maxi)
        return maxi[0]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.right = TreeNode(6)
root.left.right.right.right = TreeNode(7)

solution = Solution()

maxPathSum = solution.maxPathSum(root)
print("Maximum Path Sum:", maxPathSum)
