from .longest_increasing_subsequence import Solution


class TestLongestIncreasingSubsequence:
    def test_case_one(self):
        s = Solution()
        assert s.lengthOfLIS(nums=[9,1,4,2,3,3,7]) == 4

    def test_case_two(self):
        s = Solution()
        assert s.lengthOfLIS(nums=[0,3,1,3,2,3]) ==  4
