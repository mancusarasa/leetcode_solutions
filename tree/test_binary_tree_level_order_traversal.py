#!/usr/bin/env python3
from .binary_tree_level_order_traversal import Solution, TreeNode


class TestBinaryTreeLevelOrderTraversal:
    def test_three_level_traversal(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        s = Solution()
        assert s.levelOrder(root) == [[3], [9, 20], [15, 7]]

    def test_one_level_traversal(self):
        root = TreeNode(1)
        s = Solution()
        assert s.levelOrder(root) == [[1]]

    def test_zero_level_traversal(self):
        s = Solution()
        assert s.levelOrder(None) == []
