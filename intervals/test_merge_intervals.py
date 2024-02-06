#!/usr/bin/env python3
from .merge_intervals import Solution


class TestMergeIntervals:
    def test_case_one(self):
        s = Solution()
        assert s.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]

    def test_case_two(self):
        s = Solution()
        assert s.merge([[1,4],[4,5]]) == [[1,5]]
