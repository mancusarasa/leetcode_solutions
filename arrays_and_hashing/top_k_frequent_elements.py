#!/usr/bin/env python3
'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

'''

import heapq
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)
        for num in nums:
            frequencies[num] += 1
        most_frequent = []
        for frequency, num in frequencies.items():
            t = (-frequency, num)
            heapq.heappush(most_frequent, t)
        result = [heapq.heappop(most_frequent)[1] for _ in range(k)]
        return result
