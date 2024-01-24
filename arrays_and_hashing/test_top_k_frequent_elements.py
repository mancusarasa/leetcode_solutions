#!/usr/bin/env python3

from .top_k_frequent_elements import Solution


class TestTopKFrequentElements:
    def test_one(self):
        s = Solution()
        assert s.topKFrequent([1,1,1,2,2,3], 2) == [1, 2]

    def test_two(self):
        s = Solution()
        assert s.topKFrequent([1], 1) == [1]

