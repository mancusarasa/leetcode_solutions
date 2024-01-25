#!/usr/bin/env python3

from .generate_parentheses import Solution

class TestGenerateParentheses:
    def test_three_levels(self):
        s = Solution()
        assert s.generateParenthesis(3) == ["((()))","(()())","(())()","()(())","()()()"]

    def test_one_level(self):
        s = Solution()
        assert s.generateParenthesis(1) == ["()"]
