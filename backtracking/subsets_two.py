#!/usr/bin/env python3
'''
Given an integer array nums that may contain duplicates, return all possible
subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:

Input: nums = [0]
Output: [[],[0]]
'''
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums = sorted(nums)
        combinations = []
        current_combo = []
        def backtrack(current_index):
            if current_index == N:
                combinations.append(current_combo.copy())
                return
            current_number = nums[current_index]
            current_combo.append(current_number)
            backtrack(current_index +  1)
            current_combo.pop()
            following_index = current_index
            while following_index < N and nums[following_index] == current_number:
                following_index += 1
            backtrack(following_index)
        
        backtrack(0)
        return combinations
