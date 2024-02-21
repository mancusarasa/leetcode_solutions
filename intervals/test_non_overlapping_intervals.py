#!/usr/bin/env python3
from .non_overlapping_intervals import Solution


class TestNonOverlappingIntervals:
    def test_case_one(self):
        s = Solution()
        assert s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1

    def test_case_two(self):
        s = Solution()
        assert s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2

    def test_case_three(self):
        s = Solution()
        assert s.eraseOverlapIntervals([[1,2],[2,3]]) == 0
