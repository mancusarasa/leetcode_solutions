#!/usr/bin/env python3
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            current_profit = price - min_price
            max_profit = max(max_profit, current_profit)
            min_price = min(min_price, price)

        return max_profit
