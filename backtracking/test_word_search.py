#!/usr/bin/env python3
from .word_search import Solution


class TestWordSearch:
    def test_case_one(self):
        s = Solution()
        assert s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED") == True

    def test_case_two(self):
        s = Solution()
        assert s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE") == True

    def test_case_three(self):
        s = Solution()
        assert s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB") == False
