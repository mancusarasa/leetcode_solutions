from .contains_duplicate import Solution


class TestContainsDuplicate:

    def test_one_repeated(self):
        s = Solution()
        assert s.containsDuplicate([1,2,3,1]) == True

    def test_no_repeated(self):
        s = Solution()
        assert s.containsDuplicate([1,2,3,4]) == False


    def test_multiple_repeated(self):
        s = Solution()
        assert s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True
