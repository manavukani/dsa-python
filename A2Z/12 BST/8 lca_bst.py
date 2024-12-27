class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# simpler than BT, just find node whenr both n1 and n2 are on different sides
def lca_bst(root, n1, n2):
    if not root:
        return None
    
    while root:
        if root.val > n1 and root.val > n2:
            root = root.left
        elif root.val < n1 and root.val < n2:
            root = root.right
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
print(lca_bst(root, n1, n2).val)  # 20