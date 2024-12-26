class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# simpler than BT, just find node whenr both n1 and n2 are on different sides
def lca_bst(root, n1, n2):
    if not root:
        return None
    
    while root:
        # both on the left
        if root.data > n1 and root.data > n2:
            root = root.left
        # both on the right
        elif root.data < n1 and root.data < n2:
            root = root.right
        # one on left and one on right - curr is LCA
        else:
            break
    return root

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)

n1 = 10
n2 = 22
print(lca_bst(root, n1, n2).data)  # 20