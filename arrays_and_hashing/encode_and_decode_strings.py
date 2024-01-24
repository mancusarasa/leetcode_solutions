#!/usr/bin/env python

'''
Design an algorithm to encode a list of strings to a single string.
The encoded string is then decoded back to the original list of strings.

Please implement encode and decode
'''
from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = [f'{len(string)}{string}' for string in strs]
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        l = []
        i = 0
        N = len(s)
        while i < N:
            length = int(s[i])
            string = s[i+1:i+length+1]
            l.append(string)
            i += length + 1
        return l
