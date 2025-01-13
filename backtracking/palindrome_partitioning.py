#!/usr/bin/env python3
"""
Palindrome Partitioning

Given a string s, split s into substrings where every
substring is a palindrome. Return all possible lists of palindromic substrings.

You may return the solution in any order.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
"""
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        partitions = []
        partition = []
        n = len(s)
        def backtrack(index, current_str):
            if index == n:
                if current_str == current_str[::-1]:
                    partition.append(current_str)
                    partitions.append(partition.copy())
                    partition.pop()
                return
            # partition in this position:
            # extend the current partition with
            # the string in its current position
            if current_str == current_str[::-1]:
                partition.append(current_str)
                backtrack(index+1, s[index])
                # remove the current_str from the partition
                # since we won't partition in "the other branch"
                partition.pop()

            # dont partition in this position,
            # just extend the current string
            backtrack(index+1, f'{current_str}{s[index]}')

        backtrack(1, s[0])
        return partitions
