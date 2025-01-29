class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# BRUTE FORCE
# level order traversal, add the last element of each level to the result (rightmost)
# TC: O(N)
def brute(root):
    if not root:
        return []
    
    curr = root
    from collections import deque
    q = deque([curr])
    res = []
    while q:
        level = []
        size = len(q)
        for i in range(size):
            curr = q.popleft()
            level.append(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        res.append(level[-1]) # right most node added
    return res

# OPTIMAL
# TC = O(log N) - height, O(N) in worst case - skewed tree
# recursive DFS, but "RIGHT FIRST"
def optimalRightView(root):
    if not root:
        return []
    
    res = []

    def dfs(node, level):
        if not node:
            return
        
        # first time reach that level, add the element
        if level == len(res):
            res.append(node.val)
        
        # traverse right first recursively, if available
        dfs(node.right, level+1)
        dfs(node.left, level+1)

    dfs(root, 0)

    return res

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.right.right = Node(7)

rightView = brute(root)
print("Brute", rightView)
rightView = optimalRightView(root)
print("Optimal", rightView)