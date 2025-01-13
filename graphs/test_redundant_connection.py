from .redundant_connection import Solution


class TestRedundantConnection:
    def test_case_example_one(self):
        s = Solution()
        assert s.findRedundantConnection(
            edges=[[1,2],[1,3],[3,4],[2,4]]
        ) == [2,4]

    def test_case_example_two(self):
        s = Solution()
        assert s.findRedundantConnection(
            edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
        ) == [3,4]
