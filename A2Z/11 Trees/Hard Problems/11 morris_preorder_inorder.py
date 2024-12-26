# morris traversal is a way to traverse a tree without using recursion or stack
# SC = O(1) and TC = O(N)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
========= Morris Inorder =========

TODO - after last node, we have to go back to the root node

Case 1: If current does not have left child, print current and move to right child
Case 2: If current has a left child, make current as right child of the rightmost node in current's left subtree
(inorder predecessor, we go back to the root node)
Case 3: If link already exists, print current and remove the link

- Move to the right child of current
- If current is None, traversal is complete
"""


def morris_inorder(root):
    inorder = []
    curr = root
    while curr:
        # Case 1
        if not curr.left:
            inorder.append(curr.val)
            curr = curr.right
        # Case 2
        else:
            prev = curr.left
            # go to the rightmost node, it should not point to curr
            while prev.right and prev.right != curr:
                prev = prev.right

            # points to null, create thread, move curr to left
            if not prev.right:
                prev.right = curr
                curr = curr.left
            # Case 3: thread exists, cut it
            else:
                prev.right = None
                inorder.append(curr.val)  # root node
                curr = curr.right
    return inorder


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.right = TreeNode(6)

print(morris_inorder(root))

"""
========= Morris Preorder =========

Preorder = root, left, right

We starting at root, marking the rightmost node of the left subtree as the right child of the current node

Instead of appending when we come back to the root, we append when we go to the left child (when we create the thread)

"""

def morris_preorder(root):
    preorder = []
    curr = root
    while curr:
        # Case 1
        if not curr.left:
            preorder.append(curr.val)
            curr = curr.right
        # Case 2
        else:
            prev = curr.left
            # go to the rightmost node, it should not point to curr
            while prev.right and prev.right != curr:
                prev = prev.right

            # IMPORTANT ------ append root here, when we create thread
            # points to null, create thread, move curr to left
            if not prev.right:
                prev.right = curr
                preorder.append(curr.val)
                curr = curr.left
            # Case 3: thread exists, cut it
            else:
                prev.right = None
                curr = curr.right
    return preorder


print(morris_preorder(root))
