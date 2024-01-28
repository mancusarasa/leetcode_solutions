#!/usr/bin/env python3

from .max_depth import Solution, TreeNode


class TestMaxDepth:
    def test_case_one(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)
        s = Solution()
        assert s.maxDepth(root) == 3

    def test_case_two(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        s = Solution()
        assert s.maxDepth(root) == 2

    def test_case_three(self):
        s = Solution()
        assert s.maxDepth(None) == 0
