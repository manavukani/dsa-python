# next -> return next element in inorder
# hasNext -> return True if there is next element, else False

'''
Approach:
1. start from root
2. go to leftmost node and keep adding to stack
3. when next is called, pop from stack and add right node to stack
4. hasNext -> return True if stack is not empty

Time complexity: Amortized O(1) per next call
Space complexity: O(h) - at any time, stack will have at most h elements
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root):
        self.stack = []
        # Step 2: push all left nodes to stack
        self.pushAll(root)
    
    def pushAll(self, node):
            while node:
                self.stack.append(node)
                node = node.left

    def next(self):
        # Step 3: pop from stack and add right node to stack
        curr = self.stack.pop()
        self.pushAll(curr.right)
        # return value of popped node - next element in inorder
        return curr.val

    def hasNext(self):
        # Step 4: return True if stack is not empty
        return len(self.stack) > 0

root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

bst = BSTIterator(root)
print(bst.next()) # 3
print(bst.next()) # 7
print(bst.hasNext()) # True
print(bst.next()) # 9
print(bst.hasNext()) # True
print(bst.next()) # 15
print(bst.hasNext()) # True
print(bst.next()) # 20
print(bst.hasNext()) # False



# HW - implement for prev
'''
- push all right nodes to stack
- pop from stack
- add left node to stack, push all right nodes to stack
- return value of popped node
- return True if stack is not empty

'''

class BSTIteratorHW:
    def __init__(self, root):
        self.stack = []
        self.pushAll(root)
    
    def pushAll(self, node):
            while node:
                self.stack.append(node)
                node = node.right
    
    def prev(self):
        curr = self.stack.pop()
        self.pushAll(curr.left)
        return curr.val
    
    def hasPrev(self):
        return len(self.stack) > 0


print("----- Previous -----")
bst = BSTIteratorHW(root)
print(bst.prev()) # 20
print(bst.prev()) # 15
print(bst.hasPrev()) # True
print(bst.prev()) # 9
print(bst.hasPrev()) # True
print(bst.prev()) # 7
print(bst.hasPrev()) # True
print(bst.prev()) # 3
print(bst.hasPrev()) # False