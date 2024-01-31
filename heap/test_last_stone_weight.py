from .last_stone_weight import Solution


class TestLastStoneWeight:
    def test_case_one(self):
        s = Solution()
        assert s.lastStoneWeight([2,7,4,1,8,1]) == 1

    def test_case_two(self):
        s = Solution()
        assert s.lastStoneWeight([1]) == 1
