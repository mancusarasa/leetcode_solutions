from .coin_change import Solution


class TestCoinChange:
    def test_case_one(self):
        s = Solution()
        assert s.coinChange([1,2,5], 11) == 3

    def test_no_possible_change(self):
        s = Solution()
        assert s.coinChange([2], 3) == -1

    def test_zero_amount_equals_zero_coins(self):
        s = Solution()
        assert s.coinChange([1], 0) == 0
