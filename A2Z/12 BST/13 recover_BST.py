# values of 2 nodes swapped. recover the BST, in-place, without changing its structure.

# Brute force: Inorder traversal of BST, sort it. Find 2 swapped elements and swap them in tree.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Optimal
"""
- inorder traversal of BST, just store prev to compare with curr
- find 1st swapped element, store it as first and next as middle
- find 2nd swapped element, store it as last

Case 1: if 2nd swapped element is found, swap first and last
Case 2: else swap first and middle (adjacent elements swapped)
"""

# TC = O(n), SC = O(1)


class Solution:
    def __init__(self):
        self.first = None
        self.middle = None
        self.last = None
        self.prev = None

    def inorder(self, root):
        if not root:
            return None

        self.inorder(root.left)

        # we do stuff here

        if self.prev and self.prev.val > root.val:
            # 1st violation - mark as first and middle
            if not self.first:
                self.first = self.prev
                self.middle = root
            # 2nd violation - mark as last
            else:
                self.last = root

        self.prev = root

        # we completed stuff above

        self.inorder(root.right)

    def recoverTree(self, root):

        self.inorder(root)

        # Case 1
        if self.first and self.last:
            self.first.val, self.last.val = self.last.val, self.first.val
        # Case 2
        elif self.first and self.middle:
            self.first.val, self.middle.val = self.middle.val, self.first.val
