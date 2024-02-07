#!/usr/bin/env python3
'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner
(i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot
can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:

Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        M = [[None for j in range(m)] for i in range(n)]
        def recurse(i, j, m, n):
            if i == (n-1) or j == (m-1):
                M[i][j] = 1
            if M[i][j] is None:
                M[i][j] = recurse(i+1, j, m, n) + recurse(i, j+1, m, n)
            return M[i][j]
        return recurse(0, 0, m, n)
        # return factorial(m+n-2) // ( factorial(m-1) * factorial(n-1))
