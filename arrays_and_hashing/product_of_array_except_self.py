'''
Given an integer array nums, return an array answer such that answer[i]
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

'''
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = []
        suffix_products = []
        prefix = 1
        suffix = 1
        n = len(nums)
        for i in range(n):
            prefix *= nums[i]
            suffix *= nums[n-i-1]
            prefix_products.append(prefix)
            suffix_products.insert(0, suffix)
        products = []
        for i in range(n):
            if i == 0:
                product = suffix_products[1]
            elif i == n-1:
                product = prefix_products[-2]
            else:
                product = suffix_products[i+1] * prefix_products[i-1]
            products.append(product)
        return products
