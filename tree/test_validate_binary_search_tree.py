#!/usr/bin/env python3
from .validate_binary_search_tree import Solution, TreeNode

class TestValidateBinarySearchTree:
    def test_valid_binary_search_tree_returns_true(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        s = Solution()
        assert s.isValidBST(root) == True

    def test_invalid_binary_search_tree_returns_false(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(6)
        s = Solution()
        assert s.isValidBST(root) == False
