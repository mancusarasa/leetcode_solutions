from .diameter_of_binary_tree import Solution, TreeNode


class TestDiameterOfBinaryTree:
    def test_case_one(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        s = Solution()
        assert s.diameterOfBinaryTree(root) == 3

    def test_case_two(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        s = Solution()
        assert s.diameterOfBinaryTree(root) == 1
