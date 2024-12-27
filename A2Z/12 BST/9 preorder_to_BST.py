class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# approach 1: brute force recursive approach
# TC = O(n^2), SC = O(n)
def brute(preorder):
    if not preorder:
        return None

    # root - 1st element
    root = TreeNode(preorder[0])

    # find the index where the right subtree starts
    i = 1
    while i < len(preorder) and preorder[i] < root.val:
        i += 1

    # build left and right subtree recursively
    root.left = brute(preorder[1:i])
    root.right = brute(preorder[i:])

    return root


# approach 2: sort preorder --> inorder, use inorder and preorder to build BST
# TC = O(nlogn), SC = O(n)
def better(preorder):
    def buildTree(preorder, inorder):
        if not inorder:
            return None

        root = TreeNode(preorder.pop(0))
        i = inorder.index(root.val)

        root.left = buildTree(preorder, inorder[:i])
        root.right = buildTree(preorder, inorder[i + 1 :])

        return root

    inorder = sorted(preorder)
    return buildTree(preorder, inorder)


"""
---------------------- Approach 3: Optimal Recursive Approach ----------------------

A bound is used to ensure that nodes are placed correctly in the BST:
    - For the left subtree, values must be smaller than the current root's value.
    - For the right subtree, values must be smaller than the parent's bound.

The first value in preorder is taken as the root.
The recursion progresses by incrementing the index (idx) and assigning left and right children within valid bounds.

Base Case: If the index exceeds the array or the value does not satisfy the bound, return None.

"""


# TC = O(n)
# O(N) space used in recursion stack for the worst case (skewed tree)
# SC = O(1) excluding the recursion stack
def bstFromPreorder(preorder):
    def buildTree(preorder, i, upper_bound):
        if i[0] == len(preorder) or preorder[i[0]] > upper_bound:
            return None

        node = TreeNode(preorder[i[0]])
        i[0] += 1
        node.left = buildTree(preorder, i, node.val)
        node.right = buildTree(preorder, i, upper_bound)

        return node

    # idx is list, coz passed by reference to the recursive function
    # since it will be incremented in each recursive call.
    idx = [0]
    return buildTree(preorder, idx, float("inf"))
