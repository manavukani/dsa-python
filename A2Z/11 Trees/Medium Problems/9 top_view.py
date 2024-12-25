#     1
#    / \
#   2   3
#  / \ / \
# 4  5 6  7

# OUTPUT: 4 2 1 3 7


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def top_view(root):
    from collections import deque
    if not root:
        return []
    
    # verticle posn -> first node value
    verticles = {}
    
    # (node, verticles)
    q = deque([(root, 0)])
    
    while q:
        node, v = q.popleft()
        
        # If the vertical line is not already visited, add the node
        if v not in verticles:
            verticles[v] = node.val
        
        # Add left and right children to the queue with updated vertical lines
        if node.left:
            q.append((node.left, v - 1))
        if node.right:
            q.append((node.right, v + 1))
    
    # Collect the result by sorting the keys of the dictionary
    res = [verticles[v] for v in sorted(verticles)]
    return res

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

topView = top_view(root)

print("Vertical Traversal:")
for node in topView:
    print(node, end=" ")
