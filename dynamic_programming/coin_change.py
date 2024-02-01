#!/usr/bin/env python3
'''
You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0
'''
from math import inf
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        changes = [inf for _ in range(amount + 1)]
        changes[0] = 0
        for a in range(1, amount+1):
            min_change = inf
            for coin in coins:
                if coin <= a:
                    prev_change = changes[a-coin]
                    min_change = min(min_change, 1 + prev_change)
                changes[a] = min_change
        return -1 if (changes[-1] == inf) else changes[-1]
