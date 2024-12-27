# brute force approach -- O(n^2)
'''
- for each node, check if it is BST
- if yes, count nodes, keep track of max nodes
- if no, check left and right subtrees
'''
# HEAVY APPROACH
# optimal approach -- TC = O(n), SC = O(h)
'''
current node is BST if:
    left Subtree --> largest of all node < node
    right Subtree --> smallest of all node > node

since we need to check for left and right first and then do the work
    we use postorder traversal
    

for size
    use recirsion like we do in height
    if left and right are BST, then size = left + right + 1
    
For passing the values
    https://www.youtube.com/watch?v=X0oXMdtUDwo
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class NodeValue:
    def __init__(self, minNode, maxNode, maxSize):
        self.minNode = minNode  # Minimum value in the subtree
        self.maxNode = maxNode  # Maximum value in the subtree
        self.maxSize = maxSize  # Size of the largest BST in the subtree


class Solution:
    def largestBSTSubtree(self, root):
        def largestBSTSubtreeHelper(node):
            if not node:
                return NodeValue(float('inf'), float('-inf'), 0)

            # Get values from left and right subtree of the current node
            left = largestBSTSubtreeHelper(node.left)
            right = largestBSTSubtreeHelper(node.right)

            # Current node is a BST if:
            # - The maximum value in the left subtree is less than the node's value
            # - The node's value is less than the minimum value in the right subtree
            if left.maxNode < node.val < right.minNode:
                # It's a valid BST
                return NodeValue(
                    min(node.val, left.minNode),  # Update the min value in the subtree
                    max(node.val, right.maxNode),  # Update the max value in the subtree
                    left.maxSize + right.maxSize + 1  # Add the sizes of left, right, and current node
                )

            # Otherwise, return an invalid range (so cannot compare further) and the largest size found so far
            return NodeValue(float('-inf'), float('inf'), max(left.maxSize, right.maxSize))

        # Call the helper and return the size of the largest BST
        return largestBSTSubtreeHelper(root).maxSize



# Driver code
root = TreeNode(10)
root.left = TreeNode(5, TreeNode(1), TreeNode(8))
root.right = TreeNode(15, None, TreeNode(7))

solution = Solution()
print(solution.largestBSTSubtree(root))  # 3




# class Solution:
#     def largestBSTSubtree(self, root: TreeNode) -> int:
#         def helper(node):
#             if not node:
#                 # Return (isBST, size, min_value, max_value)
#                 return (True, 0, float('inf'), float('-inf'))

#             # Post-order traversal: Process left and right subtrees first
#             left_is_bst, left_size, left_min, left_max = helper(node.left)
#             right_is_bst, right_size, right_min, right_max = helper(node.right)

#             # Check if current subtree is a BST
#             if left_is_bst and right_is_bst and left_max < node.val < right_min:
#                 # If it's a BST, calculate size and update min/max
#                 size = left_size + right_size + 1
#                 return (True, size, min(node.val, left_min), max(node.val, right_max))

#             # If not a BST, return the largest size found so far
#             return (False, max(left_size, right_size), 0, 0)

#         # Start traversal from the root
#         _, max_size, _, _ = helper(root)
#         return max_size
