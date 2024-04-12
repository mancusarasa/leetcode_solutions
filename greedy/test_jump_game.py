#!/usr/bin/env python3
from .jump_game import Solution


class TestJumpGame:
    def test_case_one(self):
        s = Solution()
        assert s.canJump([2,3,1,1,4])

    def test_case_single_element(self):
        s = Solution()
        assert not s.canJump([3,2,1,0,4])
