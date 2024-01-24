#!/usr/bin/env python3

from .two_sum import Solution


class TestTwoSum:
    def test_one(self):
        s = Solution()
        assert s.twoSum([2,7,11,15], 9) == [0, 1]

    def test_one(self):
        s = Solution()
        assert s.twoSum([3,2,4], 6) == [1, 2]

    def test_one(self):
        s = Solution()
        assert s.twoSum([3,3], 6) == [0, 1]

