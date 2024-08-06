class TreeNode():
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None
    
    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))
    
    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def traverse_in_order(self):
        if self is None: 
            return []
        return (TreeNode.traverse_in_order(self.left) + 
                [self.key] + 
                TreeNode.traverse_in_order(self.right))
    
    def display_keys(self, space='\t', level=0):
        # If the node is empty, print ∅
        if self is None:
            print(space * level + '∅')
            return
        
        # Process the right subtree first
        if self.right is not None:
            self.right.display_keys(space, level + 1)
        else:
            if not (self.left is None and self.right is None):
                print(space * (level + 1) + '∅')
        
        # Process the current node
        print(space * level + str(self.key))
        
        # Process the left subtree
        if self.left is not None:
            self.left.display_keys(space, level + 1)
        else:
            if not (self.left is None and self.right is None):
                print(space * (level + 1) + '∅')
    
    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left),  self.key, TreeNode.to_tuple(self.right)
    
    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    @staticmethod    
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node
    
tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))

tree = TreeNode.parse_tuple(tree_tuple)

print(tree)
print("Height:", tree.height())
print("Size:", tree.size())
print("InOrder:", tree.traverse_in_order())
print("Tree to Tuple:", tree.to_tuple())
print("\n")
tree.display_keys()