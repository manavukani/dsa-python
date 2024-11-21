class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# longest distance between any two nodes of that tree
# may or may not pass through the root

# the peak will have 2 children with the longest path (diameter)
# diameter = height of left subtree + height of right subtree

# check diameter for each node and return the max
# Tc = O(n)
def optimal(root):
    diameter = 0
    def dfs(root):
        nonlocal diameter
        left_height, right_height = 0, 0
        if root.left:
            left_height = dfs(root.left)
        if root.right:
            right_height = dfs(root.right)
        
        diameter = max(diameter, left_height + right_height)
        return 1 + max(left_height, right_height)
    
    dfs(root)
    return diameter


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
root.left.right.right.right = Node(7)

print(optimal(root)) # 6