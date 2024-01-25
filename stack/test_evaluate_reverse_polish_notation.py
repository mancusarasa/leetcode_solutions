#!/usr/bin/env python3


from .evaluate_reverse_polish_notation import Solution


class TestEvaluateReversePolishNotation:
    def test_sums_and_products(self):
        s = Solution()
        assert s.evalRPN(["2","1","+","3","*"]) == 9

    def test_division_and_sum(self):
        s = Solution()
        assert s.evalRPN(["4","13","5","/","+"]) == 6

    def test_all_four_operations(self):
        s = Solution()
        assert s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
