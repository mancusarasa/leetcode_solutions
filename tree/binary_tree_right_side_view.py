#!/usr/bin/env python3
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        height = self._height(root)
        result = [0 for _ in range(height)]
        def right_side(n: TreeNode, h: int):
            result[h] = n.val
            if n.left is not None:
                right_side(n.left, h+1)
            if n.right is not None:
                right_side(n.right, h+1)
            
        right_side(root, 0)
        return result

    def _height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self._height(root.left), self._height(root.right))
