#!/usr/bin/env python3
from .find_duplicate_number import Solution


class TestFindDuplicateNumber:
    def test_case_one(self):
        s = Solution()
        assert s.findDuplicate([1,3,4,2,2]) == 2

    def test_case_two(self):
        s = Solution()
        assert s.findDuplicate([3,1,3,4,2]) == 3
