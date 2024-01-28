from .count_good_nodes import Solution, TreeNode


class TestCountGoodNodes:
    def test_four_good_nodes(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.left.left = TreeNode(3)
        root.right = TreeNode(4)
        root.right.left = TreeNode(1)
        root.right.right = TreeNode(5)
        s = Solution()
        assert s.goodNodes(root) == 4

    def test_three_good_nodes(self):
        root = TreeNode(3)
        root.left = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(2)
        s = Solution()
        assert s.goodNodes(root) == 3

    def test_only_one_node(self):
        root = TreeNode(1)
        s = Solution()
        assert s.goodNodes(root) == 1
