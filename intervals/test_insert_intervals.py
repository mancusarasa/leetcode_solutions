from .insert_intervals import Solution


class TestInsertIntervals:
    def test_case_one(self):
        s = Solution()
        assert s.insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]

    def test_case_two(self):
        s = Solution()
        assert s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
