"""
Redundant Connection

You are given a connected undirected graph with n nodes
labeled from 1 to n. Initially, it contained no cycles and
consisted of n-1 edges.

We have now added one additional edge to the graph.
The edge has two different vertices chosen from 1 to n,
and was not an edge that previously existed in the graph.

The graph is represented as an array edges of length n
where edges[i] = [ai, bi] represents an edge between nodes
 ai and bi in the graph.

Return an edge that can be removed so that the graph is
still a connected non-cyclical graph. If there are multiple
answers, return the edge that appears last in the input edges.

Example 1:
Input: edges = [[1,2],[1,3],[3,4],[2,4]]
Output: [2,4]

Example 2:

Input: edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
Output: [3,4]
"""
from typing import List


class Solution:
    class DisjointSet:
        def __init__(self):
            self._parent = {}
            self._rank = {}

        def make_set(self, x: int) -> None:
            self._parent[x] = x
            self._rank[x] = 1

        def find(self, x: int) -> int:
            if self._parent[x] != x:
                self._parent[x] = self.find(self._parent[x])
            return self._parent[x]

        def union(self, x: int, y:int) -> None:
            x_root = self.find(x)
            y_root = self.find(y)
            if self._rank[x_root] > self._rank[y_root]:
                self._parent[y_root] = x_root
            elif self._rank[y_root] > self._rank[x_root]:
                self._parent[x_root] = y_root
            else:
                self._rank[x_root] += 1
                self._parent[y_root] = x_root

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = set()
        for a_i, b_i in edges:
            nodes.add(a_i)
            nodes.add(b_i)
        d = self.DisjointSet()
        for node in nodes:
            d.make_set(node)
        redundant = []
        for a_i, b_i in edges:
            if d.find(a_i) != d.find(b_i):
                d.union(a_i, b_i)
            else:
                redundant = [a_i, b_i]
        return redundant
