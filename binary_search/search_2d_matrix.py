'''
You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_index = -1
        left_row = 0
        right_row = len(matrix) - 1

        while left_row <= right_row:
            middle_row = int((left_row+right_row)/2)
            if target < matrix[middle_row][0]:
                right_row = middle_row - 1
            elif target > matrix[middle_row][-1]:
                left_row = middle_row + 1
            else:
                row_index = middle_row
                break

        if row_index == -1:
            return False

        row = matrix[row_index]
        l = 0
        r = len(row)
        while l <= r:
            middle = int((l+r)/2)
            if target < row[middle]:
                r = middle - 1
            elif row[middle] < target:
                l = middle + 1
            else:
                return True
        return False
