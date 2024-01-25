from .max_product import Solution



class TestMaxProduct:
    def test_case_one(self):
        s = Solution()
        assert s.maxProduct([2,3,-2,4]) == 6

    def test_case_two(self):
        s = Solution()
        assert s.maxProduct([-2,0,-1]) == 0
