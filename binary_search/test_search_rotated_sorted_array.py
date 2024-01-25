#!/usr/bin/env python3
from .search_rotated_sorted_array import Solution


class TestSearchRotatedSortedArray:

    def test_one(self):
        s = Solution()
        assert s.search([4,5,6,7,0,1,2], 4) == 0

    def test_two(self):
        s = Solution()
        assert s.search([4,5,6,7,0,1,2], 3) == -1

    def test_three(self):
        s = Solution()
        assert s.search([1], 0) == -1
