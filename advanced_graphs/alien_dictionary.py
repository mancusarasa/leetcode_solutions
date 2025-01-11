"""
Alien Dictionary

There is a foreign language which uses the latin alphabet,
but the order among letters is not "a", "b", "c" ... "z" as in English.

You receive a list of non-empty strings words from the dictionary, where
the words are sorted lexicographically based on the rules of this new language.

Derive the order of letters in this language. If the order is invalid, return an empty string. If there are multiple valid order of letters, return any of them.

A string a is lexicographically smaller than a string b if either of the following is true:

    - The first letter where they differ is smaller in a than in b.
    - There is no index i such that a[i] != b[i] and a.length < b.length.

Example 1:

Input: ["z","o"]
Output: "zo"

Explanation:
From "z" and "o", we know 'z' < 'o', so return "zo".

Example 2:

Input: ["hrn","hrf","er","enn","rfnn"]
Output: "hernf"

Explanation:

from "hrn" and "hrf", we know 'n' < 'f'
from "hrf" and "er", we know 'h' < 'e'
from "er" and "enn", we know get 'r' < 'n'
from "enn" and "rfnn" we know 'e'<'r'
so one possibile solution is "hernf"
"""
from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        rules = []
        n = len(words)
        for i in range(n-1):
            found_diff = False
            for char, other in zip(words[i], words[i+1]):
                if char != other:
                    rules.append([char, other])
                    found_diff = True
                    break
            if not found_diff and len(words[i]) > len(words[i+1]):
                return ''
        # now we solve a topological sort with rules
        # as the dependencies between nodes
        graph = dict()
        for word in words:
            for char in word:
                graph[char] = set()
        for a, b in rules:
            graph[a].add(b)
        unlocked = []
        for node in graph.keys():
            # if node has input degree == 0,
            # we consider it unlocked
            input_degree = 0
            for adjacent_set in graph.values():
                if node in adjacent_set:
                    input_degree += 1
            if input_degree == 0:
                unlocked.append(node)
        
        topological_sort = []
        while unlocked:
            next_node = unlocked.pop()
            topological_sort.append(next_node)
            # unlock the nodes that depended on next_node
            unlockables = list(graph[next_node])
            for unlockable in unlockables:
                graph[next_node].remove(unlockable)
                new_input_degree = 0
                for adjacent_set in graph.values():
                    if unlockable in adjacent_set:
                        new_input_degree += 1
                if new_input_degree == 0:
                    unlocked.append(unlockable)

        if len(topological_sort) < len(graph.keys()):
            return ''
        return ''.join(topological_sort)
