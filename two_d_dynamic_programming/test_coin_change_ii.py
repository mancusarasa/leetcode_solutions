from .coin_change_ii import Solution


class TestCoinChange:
    def test_case_one(self):
        s = Solution()
        assert s.change(5, [1,2,5]) == 4

    def test_case_(self):
        s = Solution()
        assert s.change(3, [2]) == 0

    def test_case_(self):
        s = Solution()
        assert s.change(10, [10]) == 1
