#!/usr/bin/env python3
'''
Given the root of a binary search tree, and an integer k, return the kth
smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
'''
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = root
        s = []
        my_k = 0
        while n or s:
            if n is not None:
                s.append(n)
                n = n.left
            else:
                n = s.pop()
                k -= 1
                if k == 0:
                    return n.val
                n = n.right
        return n.val
