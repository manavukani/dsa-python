#     1
#    / \
#   2   3
#  / \ / \
# 4  5 6  7
# The output of print this tree vertically will be:
# 4, 2, 1 5 6, 3, 7

"""
assign the levels and verticles to each node

    1 ---> (0, 0)
   / \
  2   3 ---> 2 = (-1, 1), 3 = (1, 1)
 / \ / \
4  5 6  7 ---> 4 = (-2, 2), 5 = (0, 2), 6 = (0, 2), 7 = (2, 2)

sort the nodes based on the verticles and then level
"""

from collections import defaultdict, deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# TIME COMPLEXITY: O(N log N)
def vertical_order_traversal(root):
    if not root:
        return []

    curr = root
    # queue: node, verticles, level
    q = deque([(curr, 0, 0)])

    # verticles: [(level, node.val)]
    verticles = defaultdict(list)
    while q:
        curr, v, level = q.popleft()
        verticles[v].append((level, curr.val))
        if curr.left:
            q.append((curr.left, v - 1, level + 1))
        if curr.right:
            q.append((curr.right, v + 1, level + 1))
    res = []
    for v in sorted(verticles):
        verticles[v].sort()
        res.append([val for level, val in verticles[v]])

    return res


def printResult(result):
    for level in result:
        for node in level:
            print(node, end=" ")
        print()
    print()


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # root = Node(1)
    # root.left = Node(2)
    # root.left.left = Node(4)
    # root.left.right = Node(10)
    # root.left.left.right = Node(5)
    # root.left.left.right.right = Node(6)
    # root.right = Node(3)
    # root.right.right = Node(10)
    # root.right.left = Node(9)

    verticalTraversal = vertical_order_traversal(root)

    # Print the result
    print("Vertical Traversal: ")
    printResult(verticalTraversal)
