#!/usr/bin/env python3
'''
You are given an array of non-overlapping intervals intervals
where intervals[i] = [starti, endi] represent the start and the
end of the ith interval and intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end] that represents the
start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending
order by starti and intervals still does not have any overlapping intervals (merge
overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

'''
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        N = len(intervals)
        i = 0
        result = []
        while i < N:
            new_interval = intervals[i]
            j = i + 1
            while j < N and self._overlap(new_interval, intervals[j]):
                new_interval = self._merge(new_interval, intervals[j])
                j += 1
            result.append(new_interval)
            i = j
        
        return result

    def _overlap(self, interval, other_interval):
        if interval[0] <= other_interval[0]:
            return other_interval[0] <= interval[1]
        else:
            return other_interval[0] <= interval[0] <= other_interval[1]

    def _merge(self, interval, other_interval):
        left = min(interval[0], other_interval[0])
        right = max(interval[1], other_interval[1])
        return [left, right]
