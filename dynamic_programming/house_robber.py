"""
House Robber

You are given an integer array nums where nums[i] represents the amount
of money the ith house has. The houses are arranged in a straight line,
i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

You are planning to rob money from the houses, but you cannot rob two
adjacent houses because the security system will automatically alert
the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.

Example 1:
Input: nums = [1,1,3,3]
Output: 4
Explanation: nums[0] + nums[2] = 1 + 3 = 4.

Example 2:
Input: nums = [2,9,8,3,6]
Output: 16
Explanation: nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16.
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        max_profits = [0 for _ in range(n)]
        max_profits[n-1] = nums[n-1]
        max_profits[n-2] = max(nums[n-2], nums[n-1])
        for i in range(n-3, -1, -1):
            max_profits[i] = max(nums[i] + max_profits[i+2], max_profits[i+1])
        return max_profits[0]
