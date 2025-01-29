class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
    
        curr = root
        q = deque()
        q.append(curr)
        allLevels = []
        while q:
            levelSum = 0
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                levelSum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            allLevels.append(levelSum)
        
        maxSum = max(allLevels) # find max sum out of all levels
        return 1 + allLevels.index(maxSum) # 1 based indexing for levels
