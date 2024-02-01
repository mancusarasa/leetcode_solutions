#!/usr/bin/env python3
'''
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
'''
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        current_combo = []
        N = len(candidates)
        def backtrack(current_index, current_sum):
            if current_index == N:
                return
            elem = candidates[current_index]
            current_combo.append(elem)
            new_sum = current_sum + elem
            # next_index represents the following index
            # different to the current elem. this will allow
            # the backtracking tree to split between
            # - "combinations that have the current element"
            # - "combinations that dont have the current element"
            # thus avoid repeated elements altogether
            next_index = current_index
            while next_index < N and candidates[next_index] == elem:
                next_index += 1
            if new_sum == target:
                result.append(current_combo.copy())
                current_combo.pop()
                backtrack(next_index, current_sum)
            elif new_sum < target:
                backtrack(current_index + 1, new_sum)
                current_combo.pop()
                backtrack(next_index, current_sum)
            else:
                current_combo.pop()
                backtrack(next_index, current_sum)
        backtrack(0, 0)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5], 8))
