from .max_subarray import Solution


class TestMaxSubarray:
    def test_case_one(self):
        s = Solution()
        assert s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6

    def test_case_single_element(self):
        s = Solution()
        assert s.maxSubArray([1]) == 1

    def test_case_three(self):
        s = Solution()
        assert s.maxSubArray([5,4,-1,7,8]) == 23
