from .min_cost_to_connect_all_points import Solution


class TestMinCostToConnectAllPoints:
    def test_case_one(self):
        s = Solution()
        assert s.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]) == 20

    def test_case_two(self):
        s = Solution()
        assert s.minCostConnectPoints([[3,12],[-2,5],[-4,1]]) == 18 
