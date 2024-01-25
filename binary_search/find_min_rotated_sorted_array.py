'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
'''
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        result = nums[0]
        while left <= right:
            middle = int((left+right)/2)
            if nums[left] < nums[middle] < nums[right]:
                result = nums[left]
                break
            result = min(result, nums[middle])
            if nums[left] <= nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        return result
