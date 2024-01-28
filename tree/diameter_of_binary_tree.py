#!/usr/bin/env python3
'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

Example 1:

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:

Input: root = [1,2]
Output: 1


The length of a path between two nodes is represented by the number of edges between them.
'''
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        height_left = self._max_height(root.left)
        height_right = self._max_height(root.right)
        diameter_left = self.diameterOfBinaryTree(root.left)
        diameter_right = self.diameterOfBinaryTree(root.right)
        return max(height_left + height_right, diameter_left, diameter_right)
    
    def _max_height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self._max_height(root.left), self._max_height(root.right))
