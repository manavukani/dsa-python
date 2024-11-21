class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# find left_height and right_height and check is diff. less than or equal to 1
# TC: O(n^2)
def brute_force(root):
    def dfs(root):
        if not root:
            return 0

        return 1 + max(dfs(root.left), dfs(root.right))

    if not root:
        return True

    left_height = dfs(root.left)
    right_height = dfs(root.right)

    return abs(left_height - right_height) <= 1

'''
- optimised by simultaneously checking the balance condition
- repeatedly calculating the heights of left and right subtrees at each node
- we can compute these heights in a bottom-up manner
- we can return -1 if the subtree is unbalanced at any node

- Postorder method allows us to validate balance conditions efficiently during the traversal
- calculating subtree information before moving to the parent node
- save on TC of calling the height of children over and over again

'''
# TC: O(n)
def optimal(root):
    if not root:
        return True
    
    def dfs(root):
        if not root:
            return 0

        # POSTORDER TRAVERSAL - left, right, check @ root
        # left
        left_height = dfs(root.left)
        if left_height == -1:
            return -1

        # right
        right_height = dfs(root.right)
        if right_height == -1:
            return -1

        # root
        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1
    
    return dfs(root) != -1

# root = None
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(10)
root.right.right = TreeNode(11)
root.right.right.right = TreeNode(12)
root.right.right.right.right = TreeNode(13)

print(brute_force(root)) # False
print(optimal(root)) # False