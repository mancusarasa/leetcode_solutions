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
        assert root.left.val == 7
        assert root.right.val == 2
        assert root.left.left.val == 9
        assert root.left.right.val == 6
        assert root.right.left.val == 3 
        assert root.right.right.val == 1


