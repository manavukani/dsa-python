class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TC = O(height)
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def min_node(node):
            current = node
            while current.left is not None:
                current = current.left
            return current


        if not root:
            return root

        # If key < node val ---> search left
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        # If key > node val ---> search right
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # FOUND THE NODE TO DELETE
        else:
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children:
            # Get the inorder successor (smallest in the right subtree)
            temp = min_node(root.right)

            # Copy the inorder successor's data to this node
            root.val = temp.val

            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.val)

        return root