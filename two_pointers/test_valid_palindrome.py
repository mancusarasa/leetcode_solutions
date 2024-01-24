from .valid_palindrome import Solution


class TestValidPalindrome:
    def test_valid_palindrome(self):
        s = Solution()
        assert s.isPalindrome("A man, a plan, a canal: Panama") == True

    def test_valid_palindrome_two(self):
        s = Solution()
        assert s.isPalindrome("race a car") == False

    def test_valid_palindrome_three(self):
        s = Solution()
        assert s.isPalindrome(" ") == True

