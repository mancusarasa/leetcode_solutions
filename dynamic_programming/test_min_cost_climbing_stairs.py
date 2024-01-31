from .min_cost_climbing_stairs import Solution


class TestMinCostClimbingStairs:
    def test_case_one(self):
        s = Solution()
        assert s.minCostClimbingStairs([10,15,20]) == 15

    def test_case_two(self):
        s = Solution()
        assert s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]) == 6
