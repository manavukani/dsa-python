class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    def iterative_insert(self, value):
        new_node = TreeNode(value)
        
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right
    
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)
    
    # _protected_method
    # __private_method
    def _delete_recursive(self, node, value):
        if node is None:
            return None
        
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            min_node = self._find_min(node.right)
            node.value = min_node.value
            node.right = self._delete_recursive(node.right, min_node.value)
        
        return node
    
    def _find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
    def count_nodes(self):
        return self._count_nodes_recursive(self.root)
    
    def _count_nodes_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node is not None
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)
    
    def height(self):
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node):
        if node is None:
            return -1
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return 1 + max(left_height, right_height)
    
    def is_bxst(self):
        return self._is_bst_recursive(self.root, float('-inf'), float('inf'))
    
    def _is_bst_recursive(self, node, min_value, max_value):
        if node is None:
            return True
        if node.value <= min_value or node.value >= max_value:
            return False
        return (self._is_bst_recursive(node.left, min_value, node.value) and
                self._is_bst_recursive(node.right, node.value, max_value))
    
    def get_max(self):
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.value
    
    def get_min(self):
        if not self.root:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.value
    
    '''
    in order, pre order, post order traversals

    Level order Traversal / Level order traversal in spiral form

    Iterative Preorder Traversal of Binary Tree

    Iterative Inorder Traversal of Binary Tree

    Post-order Traversal of Binary Tree using 2 stack

    Post-order Traversal of Binary Tree using 1 stack

    Preorder, Inorder, and Postorder Traversal in one Traversa
    '''
    
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)
    
    def level_order_traversal(self):
        if not self.root:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            level_size = len(queue)
            level = []
            
            for _ in range(level_size):
                node = queue.pop(0)
                level.append(node.value)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)
        
        return result
    
    def spiral_level_order_traversal(self):
        if not self.root:
            return []
        
        result = []
        deque = [self.root]
        left_to_right = True
        
        while deque:
            level_size = len(deque)
            level = []
            
            for _ in range(level_size):
                if left_to_right:
                    node = deque.pop(0)
                    level.append(node.value)
                    if node.left:
                        deque.append(node.left)
                    if node.right:
                        deque.append(node.right)
                else:
                    node = deque.pop()
                    level.append(node.value)
                    if node.right:
                        deque.insert(0, node.right)
                    if node.left:
                        deque.insert(0, node.left)
            
            result.append(level)
            left_to_right = not left_to_right
        
        return result
    
    def iterative_preorder_traversal(self):
        if not self.root:
            return []
        
        result = []
        stack = [self.root]
        
        while stack:
            node = stack.pop()
            result.append(node.value)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return result
    
    def iterative_inorder_traversal(self):
        result = []
        stack = []
        current = self.root
        
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            result.append(current.value)
            current = current.right
        
        return result
    
    def postorder_traversal_two_stacks(self):
        if not self.root:
            return []
        
        result = []
        stack1 = [self.root]
        stack2 = []
        
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        
        while stack2:
            result.append(stack2.pop().value)
        
        return result
    
    def postorder_traversal_one_stack(self):
        result = []
        stack = []
        current = self.root
        last_visited = None
        
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                peek_node = stack[-1]
                if peek_node.right and last_visited != peek_node.right:
                    current = peek_node.right
                else:
                    result.append(peek_node.value)
                    last_visited = stack.pop()
        
        return result
    
    def all_traversals_in_one(self):
        if not self.root:
            return [], [], []
        
        preorder, inorder, postorder = [], [], []
        stack = [(self.root, 1)]
        
        while stack:
            node, state = stack.pop()
            
            if state == 1:  # Pre
                preorder.append(node.value)
                stack.append((node, 2))
                if node.left:
                    stack.append((node.left, 1))
            elif state == 2:  # In
                inorder.append(node.value)
                stack.append((node, 3))
                if node.right:
                    stack.append((node.right, 1))
            else:  # Post
                postorder.append(node.value)
        
        return preorder, inorder, postorder

# Example usage:
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(9)

print(f"Number of nodes: {tree.count_nodes()}")
print(f"Is 7 in the tree? {tree.search(7)}")
print(f"Height of the tree: {tree.height()}")
print(f"Is it a BST? {tree.is_bst()}")
print(f"Maximum value: {tree.get_max()}")
print(f"Minimum value: {tree.get_min()}")

tree.delete(3)
print(f"Number of nodes after deleting 3: {tree.count_nodes()}")

print("====================== NEW METHODS ======================")
treeNew = BinaryTree()
nodes = [5, 3, 7, 1, 4, 6, 8]
for node in nodes:
    treeNew.insert(node)

print("In-order traversal:", treeNew.inorder_traversal())
print("Pre-order traversal:", treeNew.preorder_traversal())
print("Post-order traversal:", treeNew.postorder_traversal())
print("Level-order traversal:", treeNew.level_order_traversal())
print("Spiral level-order traversal:", treeNew.spiral_level_order_traversal())
print("Iterative pre-order traversal:", treeNew.iterative_preorder_traversal())
print("Iterative in-order traversal:", treeNew.iterative_inorder_traversal())
print("Post-order traversal (2 stacks):", treeNew.postorder_traversal_two_stacks())
print("Post-order traversal (1 stack):", treeNew.postorder_traversal_one_stack())

pre, in_order, post = treeNew.all_traversals_in_one()
print("All traversals in one:")
print("  Pre-order:", pre)
print("  In-order:", in_order)
print("  Post-order:", post)

