#!/usr/bin/env python3

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        prev_prev = 1
        prev = 2
        for _ in range(3, n+1):
            result = prev_prev + prev
            prev_prev = prev
            prev = result
        return result
