#!/usr/bin/env python3

from .container_with_most_water import Solution


class TestContainerWithMostWater:
    def test_one(self):
        s = Solution()
        assert s.maxArea([1,8,6,2,5,4,8,3,7]) == 49
