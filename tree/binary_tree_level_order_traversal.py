#!/usr/bin/env python3
'''
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
'''
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _max_height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self._max_height(root.left), self._max_height(root.right))

    def _recursive_level_order(self, root: TreeNode, result: List[List[int]], height: int):
        result[height].append(root.val)
        if root.left is not None:
            self._recursive_level_order(root.left, result, height + 1)
        if root.right is not None:
            self._recursive_level_order(root.right, result, height + 1)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        max_height = self._max_height(root)
        result = [[] for _ in range(max_height)]
        if max_height > 0:
            self._recursive_level_order(root, result, 0)
        return result
