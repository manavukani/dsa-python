# inplace conversion of binary tree to linked list


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# ============================== TC = O(N) and SC = O(log N) = O(height) ==============================
"""
--------- Recursive Approach ---------

- Right Left Root - Reverse Postorder Traversal

- Go to end of right subtree, then set right to prev node, left to None
- Update prev to current node
- Do this for above nodes
- Once right subtree is done, do it for left subtree
- Then at last do it for root

"""


class Solution1:
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        if root is None:
            return
        self.flatten(root.right)

        self.flatten(root.left)

        # At this point, both left and right subtrees are flattened, and 'prev'
        # is pointing to the rightmost node in the flattened right subtree.

        root.right = self.prev
        root.left = None

        # Update 'prev' to the curr for the next iteration.
        self.prev = root


# ============================== TC = O(N) and SC = O(log N) = O(height) ==============================


"""
--------- Iterative Approach Using Stack ---------


start with root, push to stack

while stack,
    - while stack is not empty, pop the top element (curr node)
    - push right child first and then left child --- so left will always be on top of stack
    - curr right = top element of stack
    - curr left to None

"""


class Solution2:
    def flatten(self, root):
        if not root:
            return

        stack = [root]

        while stack:
            curr = stack.pop()

            # Push the right child onto the stack.
            if curr.right:
                stack.append(curr.right)

            # Push the left child onto the stack.
            if curr.left:
                stack.append(curr.left)

            # Connect the right child to the next node in the stack.
            if stack:
                curr.right = stack[-1]

            # Set the left child to None to form a right-oriented linked list.
            curr.left = None


# ============================== TC = O(N) and SC = O(1) ==============================
"""
--------- MOST OPTIMAL - SC = O(1), Similar to Morris ---------

- start with curr (root)
- if left subtree exists
    - find the rightmost node 
    - connect rightmost node to curr's right child (similar to Morris)
    - connect left child of cur to curr's right pointer (break the link)
    - set left child to None (as it is now right child)
- keep moving to right child
"""


class Solution3:
    def flatten(self, root):
        curr = root
        while curr:
            # Check for left child
            if curr.left:
                # prev = rightmost node in the left subtree
                prev = curr.left
                while prev.right:
                    prev = prev.right

                # connect rightmost node (prev) to curr right child
                prev.right = curr.right

                # connect left child to curr right
                curr.right = curr.left

                # Set the left child to None
                curr.left = None

            # keep moving to right child
            curr = curr.right


# ============ Test ============


def print_preorder(root):
    if not root:
        return
    print(root.val, end=" ")
    print_preorder(root.left)
    print_preorder(root.right)


def print_flatten_tree(root):
    if not root:
        return
    print(root.val, end=" ")
    print_flatten_tree(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.right = TreeNode(6)
root.right.right = TreeNode(7)
root.right.left = TreeNode(8)

# SOL 1
print("SOL 1")
sol = Solution1()
print("Binary Tree Preorder: ", end="")
print_preorder(root)
print()
sol.flatten(root)
print("Binary Tree After Flatten: ", end="")
print_flatten_tree(root)
print()

# SOL 2
print("SOL 2")
sol = Solution2()
print("Binary Tree Preorder: ", end="")
print_preorder(root)
print()
sol.flatten(root)
print("Binary Tree After Flatten: ", end="")
print_flatten_tree(root)
print()

# SOL 3
print("SOL 3 - Optimal")
sol = Solution3()
print("Binary Tree Preorder: ", end="")
print_preorder(root)
print()
sol.flatten(root)
print("Binary Tree After Flatten: ", end="")
print_flatten_tree(root)
print()
