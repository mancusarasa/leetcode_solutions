#!/usr/bin/env python3
from .find_min_rotated_sorted_array import Solution


class TestFindMinRotatedSortedArray:
    def test_one(self):
        s = Solution()
        assert s.findMin([3,4,5,1,2]) == 1

    def test_two(self):
        s = Solution()
        assert s.findMin([4,5,6,7,0,1,2]) == 0

    def test_three(self):
        s = Solution()
        assert s.findMin([11,13,15,17]) == 11
