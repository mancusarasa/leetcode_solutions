"""
Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from the given sequence by deleting some or
no elements without changing the relative order of the remaining characters.

For example, "cat" is a subsequence of "crabt".

Example 1:
Input: nums = [9,1,4,2,3,3,7]
Output: 4

Explanation: The longest increasing subsequence is [1,2,3,7], which has a length of 4.

Example 2:
Input: nums = [0,3,1,3,2,3]
Output: 4
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        lis = [0 for _ in range(N)]
        lis[0] = 1
        max_lis = 1
        for i in range(1, N):
            prev_size = 0
            for j in range(0, i):
                if nums[j] < nums[i]:
                    prev_size = max(prev_size, lis[j])
            lis[i] = prev_size + 1
            max_lis = max(max_lis, prev_size+1)
        return max_lis
