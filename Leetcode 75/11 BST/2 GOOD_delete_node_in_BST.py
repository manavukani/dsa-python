class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def min_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# neetcode approach
def delete_node(root, key):
    if not root:
        return root

    # If key < node val ---> search left
    if key < root.val:
        root.left = delete_node(root.left, key)

    # If key > node val ---> search right
    elif key > root.val:
        root.right = delete_node(root.right, key)

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
        root.right = delete_node(root.right, temp.val)

    return root


def printInOrder(root):
    if root is None:
        return
    printInOrder(root.left)
    print(root.val, end=" ")
    printInOrder(root.right)


# Driver code
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

printInOrder(root)
print()
printInOrder(delete_node(root, 30))
