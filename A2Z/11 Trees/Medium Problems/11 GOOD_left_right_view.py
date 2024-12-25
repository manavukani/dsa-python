# right view of a binary tree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

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
        res.append(level[-1])
    return res

# TC = O(log N) - height, O(N) in worst case - skewed tree
# recursive depth-first traversal, but RIGHT CHILD FIRST
# store the first element of each level in the result
def optimal(root):
    if not root:
        return []
    
    res = []
    def dfs(node, level):
        if not node:
            return
        # if the level is equal to the length of the result, add the node value to the result
        # first time we reach a level, add first element of that level
        if level == len(res):
            res.append(node.val)
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
rightView = optimal(root)
print("Optimal", rightView)