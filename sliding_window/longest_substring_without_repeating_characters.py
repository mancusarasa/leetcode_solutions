#!/usr/bin/env python3
'''
Given a string s, find the length of the longest
substring
without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        starting_index = 0
        indices = {}
        current_substring = 0
        for current_index, num in enumerate(s):
            if num in indices and indices[num] >= starting_index:
                # this means that num is repeated
                # within the subsequence i'm considering
                starting_index = indices[num] + 1
                current_substring = current_index - starting_index + 1
                indices[num] = current_index
            else:
                # this means I can add it without repeating
                # numbers
                current_substring += 1
                indices[num] = current_index
            longest_substring = max(longest_substring, current_substring)

        return longest_substring
