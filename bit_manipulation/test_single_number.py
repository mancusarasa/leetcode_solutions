from .single_number import Solution


class TestSingleNumber:
    def test_case_one(self):
        s = Solution()
        assert s.singleNumber([2,2,1]) == 1

    def test_case_one(self):
        s = Solution()
        assert s.singleNumber([4,1,2,1,2]) == 4

    def test_case_one(self):
        s = Solution()
        assert s.singleNumber([1]) == 1
