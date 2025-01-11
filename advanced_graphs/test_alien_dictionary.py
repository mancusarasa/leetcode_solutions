from .alien_dictionary import Solution


class TestAlienDictionary:
    def test_invalid_supplied_order_returns_empty_string(self):
        s = Solution()
        assert s.foreignDictionary(words=['wrtkj', 'wrt']) == ''

    def test_case_example_one(self):
        s = Solution()
        assert s.foreignDictionary(words=['z','o']) == 'zo'

    def test_case_example_two(self):
        s = Solution()
        assert s.foreignDictionary(['hrn','hrf','er','enn','rfnn']) == 'hernf'

    def test_case_alphabet_with_one_char(self):
        s = Solution()
        assert s.foreignDictionary(['z', 'z']) == 'z'

    def test_case_one_that_failed_in_neetcode(self):
        s = Solution()
        assert s.foreignDictionary(words=["wrt","wrf","er","ett","rftt","te"]) == 'wertf'
