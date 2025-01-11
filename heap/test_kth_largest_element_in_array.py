from .kth_largest_element_in_array import Solution


class TestKthLargestElementInArray:
    def test_case_one(self):
        s = Solution()
        assert s.findKthLargest(
            nums=[2,3,1,5,4],
            k=2
        ) == 4

    def test_case_two(self):
        s = Solution()
        assert s.findKthLargest(
            nums=[2,3,1,1,5,5,4],
            k=3
        ) == 4
