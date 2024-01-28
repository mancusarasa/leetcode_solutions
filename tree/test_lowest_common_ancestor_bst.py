#!/usr/bin/env python3
from .lowest_common_ancestor_bst import Solution, TreeNode

class TestLowestCommonAncestor:
    def test_case_one(self):
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        two = root.left
        eight = root.right
        s = Solution()
        assert s.lowestCommonAncestor(root, two, eight) == root

    def test_case_two(self):
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        two = root.left
        four = root.left.right
        s = Solution()
        assert s.lowestCommonAncestor(root, two, four) == two

    def test_case_three(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        two = root
        one = root.left
        s = Solution()
        assert s.lowestCommonAncestor(root, two, one) == root
