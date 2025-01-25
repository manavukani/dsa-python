from collections import deque

# good if in the path from root to X there are no nodes with a value greater than X


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursive DFS
# compare with previus val and check if bigger during dfs
def goodNodesDFS(root):
    def dfs(node, prev_val):
        if not node:
            return 0
        elif node.val >= prev_val:
            return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
        else:
            return dfs(node.left, prev_val) + dfs(node.right, prev_val)
    return dfs(root, root.val)


# using BFS
# keeping track of the biggest val in the path
def goodNodes(root):
    ans = 0
    q = deque()
    # q.append((root, float("-inf")))
    q.append((root, root.val))  # root is always good node

    while q:
        node, maxVal = q.popleft()
        if node.val >= maxVal:
            ans += 1

        if node.left:
            q.append((node.left, max(node.val, maxVal)))
        if node.right:
            q.append((node.right, max(node.val, maxVal)))

    return ans
