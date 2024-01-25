#!/usr/bin/env python3
from .search_2d_matrix import Solution


class TestSearch2dMatrix:
    def test_target_exists(self):
        s = Solution()
        assert s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True

    def test_target_doesnt_exist(self):
        s = Solution()
        assert s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13) == False
