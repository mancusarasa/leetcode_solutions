#!/usr/bin/env python3

from .best_time_to_buy_and_sell_stock import Solution


class TestBestTimeToBuyAndSellStock:
    def test_one(self):
        s = Solution()
        assert s.maxProfit([7,1,5,3,6,4]) == 5

    def test_no_possible_profit(self):
        s = Solution()
        assert s.maxProfit([7,6,4,3,1]) == 0
