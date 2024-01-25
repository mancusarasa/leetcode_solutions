#!/usr/bin/env python3


from .valid_parentheses import Solution


class TestValidParentheses:
    def test_single_parentheses_matching_returns_true(self):
        s = Solution()
        assert s.isValid("()") == True

    def test_multiple_matching_parentheses_no_nesting_returns_true(self):
        s = Solution()
        assert s.isValid("()[]{}") == True

    def test_assert_mismatching_returns_false(self):
        s = Solution()
        assert s.isValid("(]") == False
