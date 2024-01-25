#!/usr/bin/env python3

from .permutations import Solution


class TestPermutations:
    def test_case_one(self):
        s = Solution()
        assert s.permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    def test_case_two(self):
        s = Solution()
        assert s.permute([0,1]) == [[0,1],[1,0]]

    def test_case_three(self):
        s = Solution()
        assert s.permute([1]) == [[1]]
