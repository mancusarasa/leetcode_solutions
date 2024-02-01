from .k_closest_points_to_origin import Solution


class TestKClosestPointsToOrigin:
    def test_case_one(self):
        s = Solution()
        assert s.kClosest([[1,3],[-2,2]], 1) == [[-2, 2]]

    def test_case_two(self):
        s = Solution()
        assert s.kClosest([[3,3],[5,-1],[-2,4]], 2) == [[3,3], [-2, 4]]
