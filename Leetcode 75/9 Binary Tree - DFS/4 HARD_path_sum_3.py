# PART 3 - return number of valid paths, but they can start from individual nodes as well
class PathSum3:
    pass


# PART 1 - basic pathsum - reutrn True if any path sum = target
def hasPathSum(root, targetSum):
    if not root:
        return False

    if not root.left and not root.right:
        return root.val == targetSum

    lsum = hasPathSum(root.left, targetSum - root.val)
    rsum = hasPathSum(root.right, targetSum - root.val)

    return lsum or rsum


# PART 2 - return list of all paths whose sum is equal to target
class PathSum2:
    def dfs(self, root, current_path, ans, remainingSum):
        if not root:
            return
        current_path.append(root.val)
        if not root.left and not root.right and remainingSum == root.val:
            ans.append(current_path[::])  # found valid path

        # check for left and right subtree
        self.dfs(root.left, current_path, ans, remainingSum - root.val)
        self.dfs(root.right, current_path, ans, remainingSum - root.val)

        # backtrack
        current_path.pop()

    def pathSum(self, root, targetSum):
        ans = []
        self.dfs(root, [], ans, targetSum)
        return ans
