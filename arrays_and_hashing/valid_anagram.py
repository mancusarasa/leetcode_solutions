#!/usr/bin/env python3

'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
 
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = {}
        for c in s:
            count = h.setdefault(c, 0)
            h[c] = count + 1
        for c in t:
            count = h.get(c, 0)
            if count == 0:
                return False
            h[c] -= 1
        for c, count in h.items():
            if count > 0:
                return False
        return True
