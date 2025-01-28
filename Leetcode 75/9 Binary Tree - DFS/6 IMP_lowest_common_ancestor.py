"""
Possible Cases:
1. The node itself is one of the target nodes
2. The targets are in the left and right subtrees of the node
3. Both targets are in the same subtree


TC: O(n) 
In the worst case, each node in the tree is visited once, and 'n' is the total number of nodes.

SC: O(n)
Due to the recursive nature of the algorithm, in the worst-case scenario (a completely unbalanced tree), the call stack can grow up to 'n' layers deep.
"""

# TC = SC = O(n)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, n1, n2):

        # if curr = target node, return curr --- Case 1
        if not root or root == n1 or root == n2:
            return root
    
        # check left and right subtrees
        left = self.lowestCommonAncestor(root.left, n1, n2)
        right = self.lowestCommonAncestor(root.right, n1, n2)
        

        # If one in left subtree and other in right
        # current node is the LCA ---- Case 2
        if left and right:
            return node
        
        # If both targets are found in same subtree, LCA is in that subtree ---- Case 3
        # only 1 is not None, return the non-None -- that is where p or q is found 
        return left or right