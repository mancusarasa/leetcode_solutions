#!/usr/bin/env python3
from .cheapest_flights_within_k_stops import Solution


class TestCheapestFlightsWithinKStops:
    def test_case_one(self):
        s = Solution()
        assert s.findCheapestPrice(4, [[0,1,100], [1,2,100], [2,0,100], [1,3,600], [2,3,200]], 0, 3, 1) == 700

    def test_case_two(self):
        s = Solution()
        assert s.findCheapestPrice(3, [[0,1,100], [1,2,100], [0,2,500]], 0, 2, 1) == 200

    def test_case_three(self):
        s = Solution()
        assert s.findCheapestPrice(3, [[0,1,100], [1,2,100], [0,2,500]], 0, 2, 0) == 500
