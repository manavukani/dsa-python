class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
Build Left Subtree:
    Create the left subtree recursively:
    inorder[:mid] represents the inorder traversal of the left subtree.
    postorder[:mid] represents the postorder traversal of the left subtree.
    
Build Right Subtree:
    Create the right subtree recursively:
    inorder[mid+1:] represents the inorder traversal of the right subtree.
    postorder[mid:-1] represents the postorder traversal of the right subtree. (We exclude the last element (root_val) from postorder)

'''

class Solution:
    def buildTree(self, inorder, postorder):
        # base case => leaf node or empty list
        if not inorder or not postorder:
            return None

        root_val = postorder.pop() # last element of postorder is root
        root = TreeNode(root_val)
        mid = inorder.index(root_val) # find root in inorder

        # postorder => go till mid
        root.left = self.buildTree(inorder[:mid], postorder[:mid])

        # postorder => exclude root, go from mid 
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:]) 

        return root


# test code
def printInorder(root):
    if not root:
        return
    printInorder(root.left)
    print(root.val, end=" ")
    printInorder(root.right)


def printList(lst):
    for item in lst:
        print(item, end=" ")
    print()


inorder = [40, 20, 50, 10, 60, 30]
postorder = [40, 50, 20, 60, 30, 10]

print("Inorder List: ", end="")
printList(inorder)

print("Postorder List: ", end="")
printList(postorder)

sol = Solution()
root = sol.buildTree(inorder, postorder)

print("Inorder of Unique Binary Tree Created:")
printInorder(root)
print()
