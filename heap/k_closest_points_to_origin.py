#!/usr/bin/env python3
'''
'''
from typing import List
from math import sqrt
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance = sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(heap, (distance, point))
        return [elem[1] for elem in heapq.nsmallest(k, heap)]
