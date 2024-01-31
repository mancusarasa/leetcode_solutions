#!/usr/bin/env python3
'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

'''
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_prev = 0
        cost_prev_prev = 0
        min_cost = 0
        N = len(cost)
        for i in range(2, N+1):
            min_cost = min(cost[i-2] + cost_prev_prev, cost[i-1] + cost_prev)
            cost_prev_prev = cost_prev
            cost_prev = min_cost
        return min_cost
