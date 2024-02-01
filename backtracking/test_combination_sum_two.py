#!/usr/bin/env python3
from .combination_sum_two import Solution


class TestCombinationSumTwo:
    def test_case_one(self):
        s = Solution()
        assert s.combinationSum2([10,1,2,7,6,1,5], 8) == [[1,1,6], [1,2,5], [1,7], [2,6]]

    def test_case_two(self):
        s = Solution()
        assert s.combinationSum2([2,5,2,1,2], 5) == [[1,2,2], [5]]
