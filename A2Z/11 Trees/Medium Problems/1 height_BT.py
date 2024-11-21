class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs(root):
    if not root:
        return 0

    return 1 + max(dfs(root.left), dfs(root.right))


def bfs(root):
    from collections import deque
    
    if not root:
        return 0

    q = deque()
    q.append(root)

    height = 0

    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        height += 1
        
    return height


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(dfs(root))  # 3
print(bfs(root))  # 3