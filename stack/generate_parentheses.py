#!/usr/bin/env python3
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]
'''

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        s = []
        def recursive_generate(open_count, closed_count):
            if open_count == n and closed_count == n:
                result.append(''.join(s))
                return
            if open_count < n:
                s.append("(")
                recursive_generate(open_count+1, closed_count)
                s.pop()
            if closed_count < open_count:
                s.append(")")
                recursive_generate(open_count, closed_count+1)
                s.pop()

        recursive_generate(0, 0)
        return result
