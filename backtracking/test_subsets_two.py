#!/usr/bin/env python3

from .subsets_two import Solution


class TestSubsetsTwo:
    def test_case_one(self):
        s = Solution()
        assert s.subsetsWithDup([1,2,2]) == [[1,2,2],[1,2],[1],[2,2],[2],[]]

    def test_case_two(self):
        s = Solution()
        assert s.subsetsWithDup([0]) == [[0], []]
