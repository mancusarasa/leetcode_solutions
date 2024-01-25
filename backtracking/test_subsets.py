#!/usr/bin/env python3

from .subsets import Solution


class TestSubsets:
    def test_case_one(self):
        s = Solution()
        assert s.subsets([1,2,3]) == [[1,2,3], [1,2], [1,3], [1], [2,3], [2], [3], []]

    def test_case_two(self):
        s = Solution()
        assert s.subsets([0]) == [[0], []]
