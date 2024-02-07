#!/usr/bin/env python3
from .longest_common_subsequence import Solution


class TestLongestCommonSubsequence:
    def test_case_one(self):
        s = Solution()
        assert s.longestCommonSubsequence('abcde', 'ace') == 3

    def test_case_two(self):
        s = Solution()
        assert s.longestCommonSubsequence('abc', 'abc') == 3

    def test_case_three(self):
        s = Solution()
        assert s.longestCommonSubsequence('abc', 'def') == 0
