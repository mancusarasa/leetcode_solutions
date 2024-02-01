'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells
are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
'''
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        N = len(word)
        board_rows = len(board)
        board_cols = len(board[0])
        seen_indices = set()
        def backtrack(i: int, j: int, curr_index: int) -> bool:
            letter = word[curr_index]
            if letter != board[i][j]:
                return False
            elif curr_index == N - 1:
                return True
            neighbours = []
            if i > 0 and (i-1, j) not in seen_indices:
                neighbours.append((i-1, j))
            if i + 1 < board_rows and (i+1, j) not in seen_indices:
                neighbours.append((i+1, j))
            if j > 0 and (i, j-1) not in seen_indices:
                neighbours.append((i, j-1))
            if j + 1 < board_cols and (i, j+1) not in seen_indices:
                neighbours.append((i, j+1))
            seen_indices.add((i, j))
            for neighbour in neighbours:
                if backtrack(neighbour[0], neighbour[1], curr_index + 1):
                    return True 
            seen_indices.remove((i, j))
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if backtrack(i, j, 0):
                    return True
        return False
