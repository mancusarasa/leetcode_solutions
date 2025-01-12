from .rotate_image import Solution


class TestRotateImage:
    def test_two_by_two_image(self):
        s = Solution()
        m = [[1,2], [3,4]]
        s.rotate(m)
        assert m == [
            [3,1],
            [4,2]
        ]

    def test_three_by_three_image(self):
        s = Solution()
        m = [[1,2,3], [4,5,6], [7,8,9]]
        s.rotate(m)
        assert m == [
            [7,4,1],
            [8,5,2],
            [9,6,3],
        ]

    def test_four_by_four_image(self):
        s = Solution()
        m = [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16],
        ]
        s.rotate(m)
        assert m == [
            [13,9,5,1],
            [14,10,6,2],
            [15,11,7,3],
            [16,12,8,4],
        ]
