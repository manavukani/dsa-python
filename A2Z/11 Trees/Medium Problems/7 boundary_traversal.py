# divide into 3 parts

# root + left boundary traversal
#   - check for left
#   - check if not left then right
#   - if reach leaf node then add to result

# leaf nodes
#   - do preorder traversal - root, left, right

# right boundary traversal
#   - start from next to root
#   - check for right
#   - check if not right then left
#   - if reach leaf node then reverse (pop and add to original stack), add to result

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def isLeaf(root):
    return not root.left and not root.right

# TC = O(logn)
def left_boundary(root, res):
    curr = root.left
    while curr:
        if not isLeaf(curr):
            res.append(curr.data)
        if curr.left:
            curr = curr.left
        # if not left then right
        else:
            curr = curr.right

# TC = O(logn)
def right_boundary(root, res):
    curr = root.right
    stack = []
    while curr:
        if not isLeaf(curr):
            stack.append(curr.data)
        if curr.right:
            curr = curr.right
        # if not right then only left
        else:
            curr = curr.left

    # reversed order
    while stack:
        res.append(stack.pop())

# TC = O(n)
def leaf_nodes(root, res):
    if isLeaf(root):
        res.append(root.data)
        return
    if root.left:
        leaf_nodes(root.left, res)
    if root.right:
        leaf_nodes(root.right, res)

# overall TC = O(n)
# SC = O(n) for stack (Auxiliary space)
def boundary_traversal(root):
    if not root:
        return []
    res = [root.data]
    left_boundary(root, res)
    leaf_nodes(root, res)
    right_boundary(root, res)
    return res


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(boundary_traversal(root))  # [1, 2, 4, 5, 6, 7, 3]