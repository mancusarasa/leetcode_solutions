from .binary_search import Solution


class TestBinarySearch:
    def test_target_exists(self):
        s = Solution()
        assert s.search([-1,0,3,5,9,12], 9) == 4

    def test_target_doesnt_exist(self):
        s = Solution()
        assert s.search([-1,0,3,5,9,12], 2) == -1
