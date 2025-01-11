"""
Kth Largest Element in an Array

Given an unsorted array of integers nums
and an integer k, return the kth largest element in the array.

By kth largest element, we mean the kth largest
element in the sorted order, not the kth distinct element.

Follow-up: Can you solve it without sorting?

Example 1:
Input: nums = [2,3,1,5,4], k = 2
Output: 4

Example 2:
Input: nums = [2,3,1,1,5,5,4], k = 3
Output: 4
"""
from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap = [nums[i] for i in range(k)]
        heapq.heapify(heap)
        for i in range(k, n):
            smallest = heapq.heappop(heap)
            heapq.heappush(heap, max(smallest, nums[i]))
        return heapq.heappop(heap)
