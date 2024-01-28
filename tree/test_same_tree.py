#!/usr/bin/env python3
from .same_tree import Solution, TreeNode


class TestSameTree:
    def test_case_one(self):
        root_one = TreeNode(1)
        root_one.left = TreeNode(2)
        root_one.right = TreeNode(3)
        root_two = TreeNode(1)
        root_two.left = TreeNode(2)
        root_two.right = TreeNode(3)
        s = Solution()
        assert s.isSameTree(root_one, root_two) == True

    def test_case_two(self):
        root_one = TreeNode(1)
        root_one.left = TreeNode(2)
        root_two = TreeNode(1)
        root_two.right = TreeNode(2)
        s = Solution()
        assert s.isSameTree(root_one, root_two) == False
