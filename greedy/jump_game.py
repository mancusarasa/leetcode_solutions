#!/usr/bin/env python3
'''
You are given an integer array nums. You are initially positioned
at the array's first index, and each element in the array represents
your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
jump length is 0, which makes it impossible to reach the last index.
'''
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        current_index = N - 1
        can_jump = True
        while can_jump and current_index > 0:
            found_jump = False
            candidate = -1
            for next_position in range(current_index - 1, -1, -1):
                if current_index - next_position <= nums[next_position]:
                    candidate = next_position
                    found_jump = True
            if found_jump:
                current_index = candidate
            else:
                can_jump = False
        return current_index == 0
