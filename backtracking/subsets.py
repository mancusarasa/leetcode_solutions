#!/usr/bin/env python3
'''
Given an integer array nums of unique elements, return all possible
subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

'''

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combinations = []
        current_combination = []
        def backtrack(current_index):
            if len(nums) == current_index:
                combinations.append(current_combination.copy())
                return
            current_elem = nums[current_index]
            current_combination.append(current_elem)
            backtrack(current_index+1)
            current_combination.pop()
            backtrack(current_index+1)

        backtrack(0)
        return combinations
