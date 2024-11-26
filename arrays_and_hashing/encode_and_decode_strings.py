#!/usr/bin/env python

'''
Design an algorithm to encode a list of strings to a single string.
The encoded string is then decoded back to the original list of strings.

Please implement encode and decode
'''
from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        return ''.join((f'{len(s)}|{s}' for s in strs))
 
    def decode(self, s: str) -> List[str]:
        result = []
        current_index = 0
        N = len(s)
        while current_index < N:
            # first, parse the length of the next word
            next_word_length = 1
            while s[current_index+next_word_length] != '|':
                next_word_length += 1
            length = int(s[current_index:current_index+next_word_length])
            next_string = s[current_index+next_word_length+1:current_index+next_word_length+1+length]
            result.append(next_string)
            current_index += length + next_word_length + 1
 
        return result
