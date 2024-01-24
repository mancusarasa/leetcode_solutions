#!/usr/bin/env python3

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


class TestContainsDuplicate:

    def test_one_repeated(self):
        s = Solution()
        assert s.containsDuplicate([1,2,3,1]) == True

    def test_no_repeated(self):
        s = Solution()
        assert s.containsDuplicate([1,2,3,4]) == False


    def test_multiple_repeated(self):
        s = Solution()
        assert s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True
