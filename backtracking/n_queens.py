#!/usr/bin/env python3
'''
The n-queens puzzle is the problem of placing n queens on
an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens
puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens'
placement, where 'Q' and '.' both indicate a
queen and an empty space, respectively.


Example 1:

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:

Input: n = 1
Output: [["Q"]]

'''
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        current_combo = []
        solutions = []
        def backtrack(row):
            if row == n:
                solutions.append(current_combo.copy())
                return
            used_columns = set(p[1] for p in current_combo)
            for col in range(n):
                if col in used_columns:
                    continue
                valid_candidate = True
                for queen_pos in current_combo:
                    if abs(queen_pos[0] - row) == abs(queen_pos[1] - col):
                        valid_candidate = False
                if valid_candidate:
                    current_combo.append((row, col))
                    backtrack(row + 1)
                    current_combo.pop()
        
        backtrack(0)
        # this piece of shit part is dedicated to formatting
        # the output according to what leetcode expects
        output = []
        for solution in solutions:
            current_solution = []
            for position in solution:
                row = ['Q' if j == position[1] else '.' for j in range(n)]
                current_solution.append(''.join(row))
            output.append(current_solution)

        return output
