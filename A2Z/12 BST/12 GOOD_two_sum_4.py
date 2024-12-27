# brute force ---> do inoorder traversal and store in a list (sorted) and then check if the sum exists in the list (Two Sum 2)
# TC - O(n) + O(n) = O(n)
# SC - O(n)


def brute(root, target):
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)
    
    arr = inorder(root)  # sorted array
    i, j = 0, len(arr) - 1

    while i < j:
        if arr[i] + arr[j] == target:
            return True
        elif arr[i] + arr[j] < target:
            i += 1
        else:
            j -= 1

    return False


# ----------- Better Approach - using BST Iterator -----------
# TC = O(N)
# SC = O(H) + O(H) = O(H) -----> better than brute force
"""
i = nextIterator
j = prevIterator

if i + j > target: we need to decrease j
if i + j < target: we need to increase i
if i + j == target: return True
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root, reverse=True):
        self.stack = []
        self.reverse = reverse  # True for prev, False for next
        self.pushAll(root)

    def pushAll(self, node):
        while node:
            self.stack.append(node)
            # for next -> push all left
            # for prev -> push all right
            node = node.right if self.reverse else node.left

    def next(self):
        curr = self.stack.pop()
        if self.reverse:
            self.pushAll(curr.left)
        else:
            self.pushAll(curr.right)
        return curr.val

    def hasNext(self):
        return len(self.stack) > 0


class Solution:

    def twoSum(self, root, target):
        if not root:
            return False

        l = BSTIterator(root, False)  # next iterator
        r = BSTIterator(root, True)  # prev iterator

        i = l.next()
        j = r.next()

        while i < j:
            if i + j == target:
                return True
            elif i + j < target:
                i = l.next()
            else:
                j = r.next()

        return False


root = TreeNode(15)
root.left = TreeNode(10)
root.right = TreeNode(20)
root.left.left = TreeNode(8)
root.left.right = TreeNode(12)
root.right.left = TreeNode(17)
root.right.right = TreeNode(25)

sol = Solution()
print(sol.twoSum(root, 29))  # True
