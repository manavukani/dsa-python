# in the mirror, left becomes right and right becomes left


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isSymmetricalHelp(left, right):
    if not left and not right:
        return True
    if not left or not right or left.val != right.val:
        return False
    # check opposite sides
    return isSymmetricalHelp(left.left, right.right) and isSymmetricalHelp(
        left.right, right.left
    )

def isSymmetrical(root):
    # if not root:
    #     return True
    return not root or isSymmetricalHelp(root.left, root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)

print(isSymmetrical(root))  # True
