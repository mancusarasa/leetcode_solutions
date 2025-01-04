#!/usr/bin/env python3
from .edit_distance import Solution


class TestEditDistance:
    def test_case_one(self):
        s = Solution()
        assert s.minDistance(word1="monkeys", word2="money") == 2

    def test_case_two(self):
        s = Solution()
        assert s.minDistance(word1 = "neatcdee", word2 = "neetcode") == 3
