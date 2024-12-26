class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# neetcode solution
class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        # preorder => exclude root, go to mid
        # inorder => go till mid-1
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])

        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        return root

# test code
def printInorder(root):
    if not root:
        return
    printInorder(root.left)
    print(root.val, end=" ")
    printInorder(root.right)

def printList(lst):
    for val in lst:
        print(val, end=" ")
    print()

inorder = [9, 3, 15, 20, 7]
preorder = [3, 9, 20, 15, 7]

print("Inorder List: ", end="")
printList(inorder)

print("Preorder List: ", end="")
printList(preorder)

sol = Solution()

root = sol.buildTree(preorder, inorder)

print("Inorder of Unique Binary Tree Created:")
printInorder(root)
print()