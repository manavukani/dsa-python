# PART 3-A - return number of valid paths, but they can start from individual nodes as well
class PathSum3Brute:
    cnt = 0
    # TC = O(n^2) in the worst case (unbalanced trees)
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(root, start, s):
            if not root:
                return
            s -= root.val 
            if s==0:
                self.cnt+=1
            dfs(root.left,False, s)
            dfs(root.right,False, s)
            if start: 
                dfs(root.left,True,sum)
                dfs(root.right,True,sum)
        
        dfs(root, True, sum)
        return self.cnt

# PART 3-B -- Using prefix sum technique
class PathSum3:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        sums = defaultdict(int)  # store prefix sums
        sums[0] = 1  # one way to make a sum of 0 - no nodes in path (base case)

        def dfs(root, total):
            count = 0
            if root:
                # Update the cumulative sum (prefix sum) for the current path
                total += root.val 
                
                # check for subpath that ends at this node and sums to targetSum
                count = sums[total - targetSum]
                
                # add the current prefix sum
                sums[total] += 1
                
                # check left and right
                count += dfs(root.left, total)
                count += dfs(root.right, total)
                
                # Backtrack: remove the current prefix sum to avoid affecting other paths
                sums[total] -= 1

            return count

        return dfs(root, 0)



# PART 1-A - basic pathsum - reutrn True if any path sum = target
def hasPathSum(root, targetSum):
    if not root:
        return False

    if not root.left and not root.right:
        return root.val == targetSum

    lsum = hasPathSum(root.left, targetSum - root.val)
    rsum = hasPathSum(root.right, targetSum - root.val)

    return lsum or rsum

# PART 1-B
def hasPathSum(root, targetSum):
    def dfs(node, curSum):
        if not node:
            return False
        
        curSum += node.val

        if not node.left and not node.right:
            return curSum == targetSum
        
        lsum = dfs(node.left, curSum)
        rsum = dfs(node.right, curSum)

        return lsum or rsum
    
    return dfs(root, 0)


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
