# level order traversal but each alternate level is reversed

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def zig_zag(root):
    res = []
    if not root:
        return res
    from collections import deque
    q = deque()
    q.append(root)

    order = True

    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if not order:
            level = level[::-1]
        res.append(level)
        order = not order
    return res

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(zig_zag(root))  # [[1], [3, 2], [4, 5, 6, 7]]