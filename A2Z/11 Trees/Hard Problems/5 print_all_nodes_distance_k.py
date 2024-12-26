# ISSUE 1: we do not have a parent pointer so we can't go up the tree
# SOLUTION 1: do BFS, use hash table to store the parent of each node

# TODO: if given target Node, do BFS in all directions, and print all nodes at distance 'k' greedily


from collections import deque


class Solution:
    def distanceK(self, root, target, k):

        # BFS to mark parents of each node
        parent_mpp = {}  # node -> parent

        def markParents(root, parent_mpp):
            queue = deque()
            queue.append(root) # same as queue = deque([root])
            while queue:
                current = queue.popleft()
                # update parent of left and right child
                if current.left:
                    parent_mpp[current.left] = current
                    queue.append(current.left)
                if current.right:
                    parent_mpp[current.right] = current
                    queue.append(current.right)

        markParents(root, parent_mpp)

        # BFS to go upto K level from target node and using our hashtable info
        visited = set()
        queue = deque([target])  # start from target node
        visited.add(target)
        # traverse upto k level
        curr_level = 0
        while queue:
            size = len(queue)
            if curr_level == k:
                break
            curr_level += 1

            for _ in range(size):
                current = queue.popleft()
                # check left exist and not visited
                if current.left and current.left not in visited:
                    queue.append(current.left)
                    visited.add(current.left)

                # right...
                if current.right and current.right not in visited:
                    queue.append(current.right)
                    visited.add(current.right)

                # parent...
                if parent_mpp.get(current) and parent_mpp[current] not in visited:
                    queue.append(parent_mpp[current])
                    visited.add(parent_mpp[current])

        result = []
        while queue:
            result.append(queue.popleft().val)
        return result


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
root.right.left = Node(0)
root.right.right = Node(8)

sol = Solution()
print(sol.distanceK(root, root.left, 2))  # [7, 4, 1]
print(sol.distanceK(root, root.left, 3))  # [0, 8]
