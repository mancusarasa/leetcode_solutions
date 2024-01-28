#!/usr/bin/env python3

from .binary_tree_right_side_view import Solution, TreeNode


class TestBinaryTreeRightSideView:
    def test_case_one(self):
        r = TreeNode(1)
        r.left = TreeNode(2)
        r.left.right = TreeNode(5)
        r.right = TreeNode(3)
        r.right.right = TreeNode(4)
        s = Solution()
        assert s.rightSideView(r) == [1,3,4]

    def test_case_two(self):
        r = TreeNode(1)
        r.right = TreeNode(3)
        s = Solution()
        assert s.rightSideView(r) == [1,3]

    def test_case_empty_tree(self):
        s = Solution()
        assert s.rightSideView([]) == []
