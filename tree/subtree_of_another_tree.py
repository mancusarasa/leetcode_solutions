#!/usr/bin/env python3
'''
Given the roots of two binary trees root and subRoot, return true
if there is a subtree of root with the same structure and node values
of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in
tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:

Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
'''
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def match(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return subRoot is None
        elif subRoot is None:
            return False
        else:
            return root.val == subRoot.val and self.match(root.left, subRoot.left) and self.match(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return subRoot is None
        elif subRoot is None:
            return True
        else:
            match = self.match(root, subRoot)
            return match or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
