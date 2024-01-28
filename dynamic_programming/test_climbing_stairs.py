#!/usr/bin/env python3

from .climbing_stairs import Solution

class TestClimbingStairs:
    def test_stairs_with_two_steps(self):
        s = Solution()
        assert s.climbStairs(2) == 2

    def test_stairs_with_three_steps(self):
        s = Solution()
        assert s.climbStairs(3) == 3
