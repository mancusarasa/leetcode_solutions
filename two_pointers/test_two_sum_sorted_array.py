from .two_sum_sorted_array import Solution


class TestTwoSumSortedArray:
    def test_one(self):
        s = Solution()
        assert s.twoSum([2,7,11,15], 9) == [1, 2]

    def test_two(self):
        s = Solution()
        assert s.twoSum([2,3,4], 6) == [1, 3]

    def test_three(self):
        s = Solution()
        assert s.twoSum([-1,0], -1) == [1, 2]
