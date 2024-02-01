from .plus_one import Solution


class TestPlusOne:
    def test_case_one(self):
        s = Solution()
        assert s.plusOne([1,2,3]) == [1,2,4]

    def test_case_two(self):
        s = Solution()
        assert s.plusOne([4,3,2,1]) == [4,3,2,2]

    def test_case_three(self):
        s = Solution()
        assert s.plusOne([9]) == [1,0]
