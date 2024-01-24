#!/usr/bin/env python3
'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_sequence = 0
        for n in nums:
            if n-1 not in num_set:
                current_length = 1
                while n+current_length in num_set:
                    current_length += 1
                longest_sequence = max(longest_sequence, current_length)
        return longest_sequence
