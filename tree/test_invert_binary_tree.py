#!/usr/bin/env python3
from .invert_binary_tree import Solution, TreeNode


class TestInvertBinaryTree:
    def test_case_one(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)
        s = Solution()
        new_root = s.invertTree(root)
        assert new_root.val == 4
        assert new_root.left.val == 7
        assert new_root.right.val == 2
        assert new_root.left.left.val == 9
        assert new_root.left.right.val == 6
        assert new_root.right.left.val == 3 
        assert new_root.right.right.val == 1

    def test_case_two(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        s = Solution()
        new_root = s.invertTree(root)
        assert new_root.val == 2
        assert new_root.right.val == 1
        assert new_root.left.val == 3
