class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1, root2):
        def getSequence(root, seq):
            if not root:
                return

            if not root.left and not root.right:
                seq.append(root.val)

            getSequence(root.left, seq)
            getSequence(root.right, seq)

        leaves1, leaves2 = [], []
        getSequence(root1, leaves1)
        getSequence(root2, leaves2)

        return leaves1 == leaves2
