"""
Target Sum

You are given an array of integers nums and an integer
target.

For each number in the array, you can choose to either
add or subtract it to a total sum.

For example, if nums = [1, 2], one possible sum would be
"+1-2=-1".

If nums=[1,1], there are two different ways to sum the input
numbers to get a sum of 0: "+1-1" and "-1+1".

Return the number of different ways that you can build the
expression such that the total sum equals target.

Example 1:

Input: nums = [2,2,2], target = 2
Output: 3

Explanation: There are 3 different ways to sum the input numbers to get a sum of 2.
+2 +2 -2 = 2
+2 -2 +2 = 2
-2 +2 +2 = 2
"""
from typing import List
from math import inf, isinf
from collections import defaultdict


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = defaultdict(lambda: defaultdict(lambda: inf))
        N = len(nums)
        def top_down(i, t):
            if i == 0 and t == 0:
                memo[i][t] = 1
            elif i == 0:
                memo[i][t] = 0
            else:
                if isinf(memo[i-1][t-nums[i-1]]):
                    memo[i-1][t-nums[i-1]] = top_down(i-1, t-nums[i-1])
                if isinf(memo[i-1][t+nums[i-1]]):
                    memo[i-1][t+nums[i-1]] = top_down(i-1, t+nums[i-1])
                memo[i][t] = memo[i-1][t-nums[i-1]] + memo[i-1][t+nums[i-1]]
            return memo[i][t]

        return top_down(N, target)
