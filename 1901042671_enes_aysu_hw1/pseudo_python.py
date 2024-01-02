class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Insertion into a BST
    def insert(self, key):
        self.root = self.insert_helper(self.root, key)

    def insert_helper(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = self.insert_helper(root.left, key)
        else:
            root.right = self.insert_helper(root.right, key)
        return root

    # # #
    # Merging two BSTs
    # To merge two BSTs, first need to convert the second tree into a list by inorder traversal, which takes O(n) time.
    # Then, for each element in the list, perform an insertion into the first tree, which takes O(h) time.
    # Therefore time complexity is O(n * h) in the worst case, where 'n' is the number of elements in the second tree, and 'h' is the height of the first tree.
    # # #
    def merge(self, other_tree):
        other_list = other_tree.inorder_traversal() 
        for element in other_list: 
            self.insert(element)

    # # #
    # Finding the kth smallest element
    # The time complexity of this code to find the kth smallest element in a binary search tree is O(h + k), 
    # ("h" is the height of the tree and "k" is the desired rank of the element)
    # In the worst case scenario where the tree is asymmetric, the time complexity is O(n).
    # # #
    def kth_smallest(self, k):
        count, result = [0], [None]
        self.kth_smallest_helper(self.root, k, count, result)
        return result[0]

    def kth_smallest_helper(self, root, k, count, result):
        if root is None:
            return
        self.kth_smallest_helper(root.left, k, count, result)
        count[0] += 1
        if count[0] == k:
            result[0] = root.key
        self.kth_smallest_helper(root.right, k, count, result)

    # # #
    # Balancing the BST
    # The time complexity of this balancing operation depends on the inorder_traversal to obtain the elements (O(n)) 
    # and the construction of the balanced tree. The construction of the balanced tree has a time complexity of O(n), 
    # where "n" is the number of elements in the tree, because you process each element once. 
    # Therefore, the overall time complexity of the balance method is O(n).
    # # #
    def balance(self):
        elements = self.inorder_traversal()
        self.root = self.balance_helper(elements)

    def balance_helper(self, elements):
        if not elements:
            return None
        mid = len(elements) // 2
        root = TreeNode(elements[mid])
        root.left = self.balance_helper(elements[:mid])
        root.right = self.balance_helper(elements[mid + 1:])
        return root

    # # #
    # Finding elements within a specified value range
    # The time complexity depends on the number of elements within the specified range. 
    # In the worst case, it's O(n), where n is the total number of elements in the tree, so it's time complexity is O(n). 
    # # #
    def find_range(self, low, high):
        result = []
        self.find_range_helper(self.root, low, high, result)
        return result

    def find_range_helper(self, root, low, high, result):
        if root is None:
            return
        if low < root.key:
            self.find_range_helper(root.left, low, high, result)
        if low <= root.key and root.key <= high:
            result.append(root.key)
        if high > root.key:
            self.find_range_helper(root.right, low, high, result)

    # Inorder traversal for testing
    def inorder_traversal(self):
        result = []
        self.inorder_traversal_helper(self.root, result)
        return result

    def inorder_traversal_helper(self, root, result):
        if root is not None:
            self.inorder_traversal_helper(root.left, result)
            result.append(root.key)
            self.inorder_traversal_helper(root.right, result)

# TEST FUNCTIONS #
def test_bst_operations():

    bst1 = BST()
    bst2 = BST()
    bst1.insert(3)
    bst1.insert(1)
    bst1.insert(5)
    bst2.insert(2)
    bst2.insert(4)
    bst2.insert(6)

    # Test Merging
    bst1.merge(bst2)
    print("Merged BST:", bst1.inorder_traversal())

    # Test Finding kth smallest element
    k = 3
    kth_smallest = bst1.kth_smallest(k)
    print(f"{k}-th smallest element:", kth_smallest)

    # Test Balancing
    bst1.insert(10)
    bst1.insert(20)
    bst1.balance()
    print("Balanced BST:", bst1.inorder_traversal())

    # Test Finding elements within a specified value range
    low, high = 2, 9
    elements_in_range = bst1.find_range(low, high)
    print(f"Elements in range [{low}, {high}]:", elements_in_range)

if __name__ == "__main__":
    test_bst_operations()

