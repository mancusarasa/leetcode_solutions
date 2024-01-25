#!/usr/bin/env python3


from .min_stack import MinStack


class TestMinStack:
    def test_multiple_operations_yields_consiting_results(self):
        s = MinStack()
        s.push(-2)
        s.push(0)
        s.push(-3)
        assert s.getMin() == -3
        s.pop()
        assert s.top() == 0
        assert s.getMin() == -2
