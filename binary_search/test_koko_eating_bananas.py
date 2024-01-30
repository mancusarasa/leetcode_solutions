from .koko_eating_bananas import Solution


class TestKokoEatingBananas:
    def test_case_one(self):
        s = Solution()
        assert s.minEatingSpeed([3,6,7,11], 8) == 4

    def test_case_two(self):
        s = Solution()
        assert s.minEatingSpeed([30,11,23,4,20], 5) == 30

    def test_case_three(self):
        s = Solution()
        assert s.minEatingSpeed([30,11,23,4,20], 6) == 23
