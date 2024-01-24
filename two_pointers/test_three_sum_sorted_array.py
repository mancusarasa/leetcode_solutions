#!/usr/bin/env python3

from .three_sum_sorted_array import Solution


class TestThreeSumSortedArray:
    def test_one(self):
        s = Solution()
        assert s.threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]

    def test_two(self):
        s = Solution()
        assert s.threeSum([0,0,0]) == [[0,0,0]]

    def test_three(self):
        s = Solution()
        assert s.threeSum([0,1,1]) == []
