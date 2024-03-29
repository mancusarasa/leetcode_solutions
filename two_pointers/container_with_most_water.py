#!/usr/bin/env python3
'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array
[1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
'''
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
        l = 0
        r = N - 1
        max_area = 0
        while l < r:
            current_area = min(height[l], height[r]) * (r-l)
            max_area = max(max_area, current_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


if __name__ == '__main__':
    s = Solution()
    s.maxArea([1,8,6,2,5,4,8,3,7])
