#!/usr/bin/env python3


from .daily_temperatures import Solution


class TestDailyTemperatures:
    def test_one(self):
        s = Solution()
        assert s.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1, 1, 4, 2, 1, 1, 0, 0]

    def test_two(self):
        s = Solution()
        assert s.dailyTemperatures([30,40,50,60]) == [1, 1, 1, 0]

    def test_three(self):
        s = Solution()
        assert s.dailyTemperatures([30,60,90]) == [1, 1, 0]
