#!/usr/bin/env python3

from .longest_substring_without_repeating_characters import Solution


class TestLongestSubstringWithoutRepeatingCharacters:
    def test_several_subsequences_size_three(self):
        s = Solution()
        assert s.lengthOfLongestSubstring("abcabcbb") == 3

    def test_all_repeated(self):
        s = Solution()
        assert s.lengthOfLongestSubstring("bbbbb") == 1

    def test_single_subsequence_size_three(self):
        s = Solution()
        assert s.lengthOfLongestSubstring("pwwkew") == 3        
