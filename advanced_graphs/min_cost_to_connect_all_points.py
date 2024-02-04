#!/usr/bin/env python3
'''
You are given an array points representing integer coordinates of
some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the
manhattan distance between them: |xi - xj| + |yi - yj|, where
|val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points
are connected if there is exactly one simple path between any two points.

Example 1:

Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
'''
from typing import List, Set
from math import inf


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        key = [inf] * N
        pred = [None] * N
        key[0] = 0
        mst_nodes = set()
        for i in range(N):
            u = self._extract_min(key, mst_nodes)
            mst_nodes.add(u)
            for v in range(N):
                if u == v:
                    continue
                w = self._manhattan(points[u], points[v])
                if (v not in mst_nodes) and (w < key[v]):
                    pred[v] = u
                    key[v] = w
        return sum(key)

    def _extract_min(self, key: List[int], mst_nodes: Set[int]):
        min_key = inf
        min_vertex = -1
        for index, key_vertex in enumerate(key):
            if key_vertex < min_key and index not in mst_nodes:
                min_vertex = index
                min_key = key_vertex
        return min_vertex

    def _manhattan(self, point_one: List[int], point_two: List[int]):
        return abs(point_one[0] - point_two[0]) + abs(point_one[1] - point_two[1])


if __name__ == '__main__':
    s = Solution()
    s.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])
