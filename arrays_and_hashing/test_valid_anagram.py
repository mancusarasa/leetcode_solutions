from .valid_anagram import Solution


class TestValidAnagram:

    def test_valid_anagram(self):
        s = Solution()
        assert s.isAnagram("anagram", "nagaram") == True

    def test_invalid_anagram(self):
        s = Solution()
        assert s.isAnagram("anagram", "nagarammmmm") == False
