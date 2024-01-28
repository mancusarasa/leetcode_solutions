#!/usr/bin/env python3

from .subtree_of_another_tree import Solution, TreeNode


class TestSubtreeOfAnotherTree:
    def test_case_actual_subtree_returns_true(self):
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        subroot = TreeNode(4)
        subroot.left = TreeNode(1)
        subroot.right = TreeNode(2)
        s = Solution()
        assert s.isSubtree(root, subroot) == True

    def test_case_not_a_subtree_returns_false(self):
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(0)
        subroot = TreeNode(4)
        subroot.left = TreeNode(1)
        subroot.right = TreeNode(2)
        s = Solution()
        assert s.isSubtree(root, subroot) == False
