#!/usr/bin/env python3
'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

'''
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        current_combo = []
        result = []
        def backtrack(free_indices):
            if len(current_combo) == N:
                result.append(current_combo.copy())
                return
            for index in free_indices:
                current_combo.append(nums[index])
                new_set = free_indices - set([index])
                backtrack(new_set)
                current_combo.pop()
        
        backtrack(set(i for i,_ in enumerate(nums)))
        return result
