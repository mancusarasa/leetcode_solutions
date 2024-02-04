#!/usr/bin/env python3
'''
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals, and return an array of the non-overlapping
intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

'''
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        N = len(intervals)
        i = 0
        result = []
        while i < N:
            current_interval = intervals[i].copy()
            j = i+1
            while j < N and self._overlap(current_interval, intervals[j]):
                current_interval = self._merge(current_interval, intervals[j])
                j += 1
            result.append(current_interval)
            i = j
        return result

    def _overlap(self, interval_one: List[int], interval_two: List[int]) -> bool:
        overlap_left = interval_two[0] <= interval_one[0] <= interval_two[1]
        overlap_right = interval_one[0] <= interval_two[0] <= interval_one[1]
        superset_left = interval_one[0] <= interval_two[0] and interval_two[1] <= interval_one[1]
        superset_right = interval_two[0] <= interval_one[0] and interval_one[1] <= interval_two[1]
        return overlap_left or overlap_right or superset_left or superset_right

    def _merge(self, interval_one: List[int], interval_two: List[int]) -> List[int]:
        left = min(interval_one[0], interval_two[0])
        right = max(interval_one[1], interval_two[1])
        return [left, right]


if __name__ == '__main__':
    s = Solution()
    print(s.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
