from .kth_largest_element_in_stream import KthLargest


class TestKthLargestElementInStream:
    def test_case_one(self):
        kthLargest = KthLargest(3, [4, 5, 8, 2])
        assert kthLargest.add(3) == 4
        assert kthLargest.add(5) == 5
        assert kthLargest.add(10) == 5
        assert kthLargest.add(9) == 8
        assert kthLargest.add(4) == 8
