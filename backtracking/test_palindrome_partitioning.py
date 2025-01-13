from .palindrome_partitioning import Solution


class TestPalindromePartitioning:
    def test_case_example_one(self):
        s = Solution()
        assert s.partition("aab") == [
            ["a", "a", "b"],
            ["aa", "b"],
        ]

    def test_case_example_two(self):
        s = Solution()
        assert s.partition("a") == [["a"]]
