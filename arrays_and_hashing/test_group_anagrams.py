#!/usr/bin/env python3


from .group_anagrams import Solution


class TestGroupAnagrams:

    def test_one(self):
        s = Solution()
        assert s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    def test_two(self):
        s = Solution()
        assert s.groupAnagrams([""]) == [[""]]

    def test_three(self):
        s = Solution()
        assert s.groupAnagrams(["a"]) == [["a"]]
