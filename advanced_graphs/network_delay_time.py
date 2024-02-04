#!/usr/bin/env python3
'''
You are given a network of n nodes, labeled from 1 to n.
You are also given times, a list of travel times as directed edges
times[i] = (ui, vi, wi), where ui is the source node, vi is the target node,
and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes
for all the n nodes to receive the signal. If it is impossible for all the n
nodes to receive the signal, return -1.

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
'''
from typing import List, Tuple, Dict, Set
from collections import namedtuple, defaultdict
from math import inf

Adjacency = namedtuple('Adjacency', 'neighbour weight')


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(set)
        for time in times:
            g[time[0]].add(Adjacency(time[1], time[2]))
        distance, predecessors = self._initialize_single_source(n, k)
        Q = set(range(1, n+1))
        while Q:
            u = self._extract_min(Q, distance)
            for adj in g[u]:
                self._relax(u, adj.neighbour, adj.weight, distance, predecessors)
        res = max(distance.values())
        return -1 if res == inf else res

    def _initialize_single_source(self, nodes_count: int, src_node: int) -> Tuple[Dict, Dict]:
        distance = {node: inf for node in range(1, nodes_count+1)}
        predecessors = {node: None for node in range(1, nodes_count+1)}
        distance[src_node] = 0
        return distance, predecessors

    def _extract_min(self, Q: Set[int], distance: Dict[int, int]):
        min_distance = inf  
        u = -1
        for node in Q:
            if distance[node] <= min_distance:
                min_distance = distance[node]
                u = node
        Q.remove(u)
        return u

    def _relax(self, u: int, v: int, weight: int, distance: Dict, predecessors: Dict):
        if distance[v] > distance[u] + weight:
            distance[v] = distance[u] + weight
            predecessors[v] = u

if __name__ == '__main__':
    s = Solution()
    print(s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
    print(s.networkDelayTime([[1,2,1]], 2, 1))
    print(s.networkDelayTime([[1,2,1]], 2, 2))
