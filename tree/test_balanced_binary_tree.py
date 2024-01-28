#!/usr/bin/env python3
from .balanced_binary_tree import Solution, TreeNode


class TestBalancedBinaryTree:
    def test_case_one(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        s = Solution()
        assert s.isBalanced(root) == True

    def test_case_two(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.left = TreeNode(2)
        root.left.right = TreeNode(3)
        root.left.left = TreeNode(3)
        root.left.left.right = TreeNode(4)
        root.left.left.left = TreeNode(4)
        s = Solution()
        assert s.isBalanced(root) == False

    def test_case_empty_tree(self):
        s = Solution()
        assert s.isBalanced(None) == True
