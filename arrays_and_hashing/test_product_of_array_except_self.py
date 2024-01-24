from .product_of_array_except_self import Solution


class TestProductOfArrayExceptSelf:

    def test_one(self):
        s = Solution()
        assert s.productExceptSelf([1,2,3,4]) == [24,12,8,6]

    def test_two(self):
        s = Solution()
        assert s.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]
