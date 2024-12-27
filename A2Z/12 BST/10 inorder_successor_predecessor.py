# naive - find inorder, then find successor


# better -- O(h) time, O(1) space
def succ(root, target):
    if not root:
        return None

    succ = None

    curr = root
    while curr:
        # curr is less than target, cant be successor, go right
        if curr.val <= target.val:
            curr = curr.right
        else:
            succ = curr
            curr = curr.left

    return succ


def pred(root, target):
    if not root:
        return None

    pred = None
    curr = root
    while curr:
        if curr.val >= target.val:
            curr = curr.left
        else:
            pred = curr
            curr = curr.right

    return pred


def succ_recursive(root, key):
    if not root:
        return None

    if root.val <= key.val:
        return succ_recursive(root.right, key)
    else:
        left = succ_recursive(root.left, key)

        if left:
            return left
        else:
            return root


def pred_recursive(root, key):
    if not root:
        return None

    if root.val >= key.val:
        return pred_recursive(root.left, key)
    else:
        right = pred_recursive(root.right, key)

        if right:
            return right
        else:
            return root


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

print(succ(root, root.right.left).val) # 9