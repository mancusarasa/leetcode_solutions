#!/usr/bin/env python3

from .combination_sum import Solution

class TestCombinationSum:
    def test_case_one(self):
        s = Solution()
        assert s.combinationSum([2,3,6,7], 7) == [[2,2,3],[7]]

    def test_case_two(self):
        s = Solution()
        assert s.combinationSum([2,3,5], 8) == [[2,2,2,2],[2,3,3],[3,5]]

    def test_case_three(self):
        s = Solution()
        assert s.combinationSum([2], 1) == []
