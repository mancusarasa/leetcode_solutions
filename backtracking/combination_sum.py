#!/usr/bin/env python3
'''
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency
of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than
150 combinations for the given input.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:

Input: candidates = [2], target = 1
Output: []

'''
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        current_combo = []
        result = []
        def backtrack(current_index, current_sum):
            if current_index == N:
                return
            current_number = candidates[current_index]
            new_sum = current_sum + current_number
            if new_sum == target:
                current_combo.append(current_number)
                result.append(current_combo.copy())
                current_combo.pop()
                backtrack(current_index+1, current_sum)
            elif new_sum < target:
                current_combo.append(current_number)
                backtrack(current_index, new_sum)
                current_combo.pop()
                backtrack(current_index+1, new_sum-current_number)
            else:
                # new_sum > target
                backtrack(current_index+1, current_sum)
        backtrack(0, 0)
        return result
                
