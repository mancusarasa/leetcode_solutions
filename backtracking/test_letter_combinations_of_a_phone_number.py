#!/usr/bin/env python3

from .letter_combinations_of_a_phone_number import Solution


class TestLetterCombinationsOfPhoneNumber:
    def test_two_digits_combinations(self):
        s = Solution()
        assert s.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    def test_empty_digit_combinations(self):
        s = Solution()
        assert s.letterCombinations("") == []

    def test_single_digit_combinations(self):
        s = Solution()
        assert s.letterCombinations("2") == ["a", "b", "c"]
