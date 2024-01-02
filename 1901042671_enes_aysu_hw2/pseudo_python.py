class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_balanced(root):
    if root is None:
        return True
    left_height = height_of_tree(root.left)
    right_height = height_of_tree(root.right)
    if abs(left_height - right_height) <= 1 and is_balanced(root.left) is True and is_balanced(root.right) is True:
        return True
    return False

def height_of_tree(root):
    if root is None:
        return 0
    return max(height_of_tree(root.left), height_of_tree(root.right)) + 1

def test():
    # Balanced tree
    root_balanced = TreeNode(1)
    root_balanced.left = TreeNode(2)
    root_balanced.right = TreeNode(3)
    root_balanced.left.left = TreeNode(4)
    root_balanced.left.right = TreeNode(5)
    root_balanced.right.left = TreeNode(6)
    root_balanced.right.right = TreeNode(7)
    print("balanced tree test:", is_balanced(root_balanced))

    # Unbalanced tree
    root_unbalanced = TreeNode(1)
    root_unbalanced.left = TreeNode(2)
    root_unbalanced.left.left = TreeNode(3)
    root_unbalanced.left.left.left = TreeNode(4)
    print("unbalanced tree test:", is_balanced(root_unbalanced))

test()