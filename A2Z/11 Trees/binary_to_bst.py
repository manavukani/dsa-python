# Python program to convert a left unbalanced 
# BST to a balanced BST

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

# Inorder traversal to store elements of the
# tree in sorted order
def store_inorder(root, nodes):
    if root is None:
        return

    # Traverse the left subtree
    store_inorder(root.left, nodes)

    # Store the node data
    nodes.append(root.data)

    # Traverse the right subtree
    store_inorder(root.right, nodes)

# Function to build a balanced BST from a sorted array
def build_balanced_tree(nodes, start, end):
    
    # Base case
    if start > end:
        return None

    # Get the middle element and make it the root
    mid = (start + end) // 2
    root = Node(nodes[mid])

    # Recursively build the left and right subtrees
    root.left = build_balanced_tree(nodes, start, mid - 1)
    root.right = build_balanced_tree(nodes, mid + 1, end)

    return root

# Function to balance a BST
def balance_bst(root):
    nodes = []

    # Store the nodes in sorted order
    store_inorder(root, nodes)

    # Build the balanced tree from the sorted nodes
    return build_balanced_tree(nodes, 0, len(nodes) - 1)

# Function to print the tree (Inorder Traversal)
def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)

if __name__ == "__main__":
    
    # Constructing an unbalanced BST
    #        10
    #       /  \
    #      5    15
    #     /       \
    #    2         20
    #   /
    #  1

    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(2)
    root.left.left.left = Node(1)
    root.right = Node(15)
    root.right.right = Node(20)

    balanced_root = balance_bst(root)
    inorder(balanced_root)
    print()
