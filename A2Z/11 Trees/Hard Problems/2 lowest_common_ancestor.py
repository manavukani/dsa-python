class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# not as simple as BST, need to check both left and right using recursion
# return null if node val not equal to n1 or n2, else return node.value
def lca(root,n1,n2):
    if not root or root.data == n1 or root.data == n2:
        return root
    
    left = lca(root.left, n1, n2)
    rigth = lca(root.right, n1, n2)
    
    if not left:
        return rigth
    elif not rigth:
        return left
    # both are not null
    else:
        return root


root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)

n1 = 10
n2 = 22
print(lca(root, n1, n2).data)  # 20