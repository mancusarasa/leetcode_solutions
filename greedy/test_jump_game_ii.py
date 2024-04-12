#!/usr/bin/env python3
from .jump_game_ii import Solution


class TestJumpGame:
    def test_case_one(self):
        s = Solution()
        assert s.jump([2,3,1,1,4]) == 2

    def test_case_single_element(self):
        s = Solution()
        assert s.jump([2,3,0,1,4]) == 2
