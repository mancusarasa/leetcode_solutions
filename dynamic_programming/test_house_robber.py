from .house_robber import Solution


class TestHouseRobber:
    def test_case_one(self):
        s = Solution()
        assert s.rob(nums=[1,1,3,3]) == 4

    def test_case_two(self):
        s = Solution()
        assert s.rob(nums=[2,9,8,3,6]) == 16
