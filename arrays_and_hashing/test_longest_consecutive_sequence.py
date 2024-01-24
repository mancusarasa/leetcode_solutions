#!/usr/bin/env python3

from .longest_consecutive_sequence import Solution

class TestLongestConsecutiveSequence:
    def test_one(self):
        s = Solution()
        assert s.longestConsecutive([100,4,200,1,3,2]) == 4

    def test_one(self):
        s = Solution()
        assert s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9
