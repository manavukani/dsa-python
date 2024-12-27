class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# uses stack to keep track of nodes
# TC = O(n)
# SC = O(n)
class NaiveSolution:
    def kthSmallest(self, root, k):
        counter = 0
        stack = []
        cur = root

        while cur or stack:
            # left
            while cur:
                stack.append(cur)
                cur = cur.left

            # root
            cur = stack.pop()
            counter += 1
            if counter == k:
                return cur.val

            # right
            cur = cur.right


# inorder and findKth from start and end
# TC = O(n)
# SC = O(n)
class NaiveRecursive:
    def inorder(self, node, arr):
        if not node:
            return
        self.inorder(node.left, arr)
        arr.append(node.val)
        self.inorder(node.right, arr)
        return

    def findKth(self, node, k):
        arr = []
        self.inorder(node, arr)
        kLargest = arr[len(arr) - k]  # kth from end
        kSmallest = arr[k - 1]  # kth from start
        return (kSmallest, kLargest)

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(13)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(2)
root.left.left.right = TreeNode(4)
root.left.right = TreeNode(6)
root.left.right.right = TreeNode(9)
root.right.left = TreeNode(11)
root.right.right = TreeNode(14)

solution = NaiveRecursive()
kthElements = solution.findKth(root, 3)
print("Kth smallest element:", kthElements[0])
print("Kth largest element:", kthElements[1])


# ========== Morris Traversal - inorder traversal without stack ==========
# TC = O(n)
# ========== SC = O(1) ==========
class MorrisTraversalSolution:
    # inorder traversal using morris traversal
    def kthSmallest(self, root, k):
        curr = root
        while curr:
            if not curr.left:
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                prev = curr.left
                while prev.right:
                    prev = prev.right

                prev.right = curr
                temp = curr
                curr = curr.left
                temp.left = None

    # reverse inorder traversal using morris traversal
    def kthLargest(self, root, k):
        curr = root
        while curr:
            if not curr.right:
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.left
            else:
                prev = curr.right
                while prev.left:
                    prev = prev.left

                prev.left = curr
                temp = curr
                curr = curr.right
                temp.right = None

    def find_kth(self, root, k):
        k_smallest = self.kthSmallest(root, k)
        k_largest = self.kthLargest(root, k)
        return k_smallest, k_largest


solution = MorrisTraversalSolution()
kthElements = solution.find_kth(root, 3)
print("Kth smallest element:", kthElements[0])
print("Kth largest element:", kthElements[1])
