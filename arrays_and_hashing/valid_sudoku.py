#!/usr/bin/env python3
'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
'''

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = len(board)
        rows = [set() for _ in range(N)]
        columns = [set() for _ in range(N)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(N):
            for j in range(N):
                box_i = int(i/3)
                box_j = int(j/3)
                if not board[i][j].isdigit():
                    continue
                n = int(board[i][j])
                if n in rows[i] or n in columns[j] or n in boxes[box_i][box_j]:
                    return False
                rows[i].add(n)
                columns[j].add(n)
                boxes[box_i][box_j].add(n)
        return True
