#!/usr/bin/env python3
from .kth_smallest_element_in_a_bst import Solution, TreeNode


class TestKthSmallestElementInBst:
    def test_case_one(self):
        r  = TreeNode(3)
        r.left = TreeNode(1)
        r.right = TreeNode(4)
        r.left.right = TreeNode(2)
        s = Solution()
        assert s.kthSmallest(r, 1) == 1

    def test_case_two(self):
        r = TreeNode(5)
        r.right = TreeNode(6)
        r.left = TreeNode(3)
        r.left.right = TreeNode(4)
        r.left.left = TreeNode(2)
        r.left.left.left = TreeNode(1)
        s = Solution()
        assert s.kthSmallest(r, 3) == 3
