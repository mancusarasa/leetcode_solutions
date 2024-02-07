#!/usr/bin/env python3
from .unique_paths import Solution


class TestUniquePaths:
    def test_case_one(self):
        s = Solution()
        assert s.uniquePaths(3, 7) == 28

    def test_case_two(self):
        s = Solution()
        assert s.uniquePaths(3, 2) == 3
