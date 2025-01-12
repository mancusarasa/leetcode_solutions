"""
Rotate Image

Given a square n x n matrix of
integers matrix, rotate it by 90 degrees clockwise.

You must rotate the matrix in-place. Do not allocate
another 2D matrix and do the rotation.

Example 1:

Input: matrix = [
  [1,2],
  [3,4]
]
Output: [
  [3,1],
  [4,2]
]

Input: matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
Output: [
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
"""
from typing import List
from math import floor


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        bands = floor(n/2)
        for band in range(bands):
            band_size = n - band*2
            offset = band
            for i in range(offset, band_size+offset-1):
                elem_one = matrix[band][i]
                elem_two = matrix[i][n-1-band]
                elem_three = matrix[n-1-band][n-1-i]
                elem_four = matrix[n-1-i][band]
                # perform the four-way swap
                matrix[i][n-1-band] = elem_one
                matrix[n-1-band][n-1-i] = elem_two
                matrix[n-1-i][band] = elem_three
                matrix[band][i] = elem_four
