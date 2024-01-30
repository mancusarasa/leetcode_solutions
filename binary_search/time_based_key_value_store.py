'''
Design a time-based key-value data structure that can store
multiple values for the same key at different time stamps and
retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the
key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that
set was called previously, with timestamp_prev <= timestamp. If there
are multiple such values, it returns the value associated with the largest
timestamp_prev. If there are no values, it returns "".
'''

from collections import defaultdict
from typing import Tuple, List


class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        t = (timestamp, value)
        l = self.store[key]
        self._insert_sorted(l, t)
        

    def get(self, key: str, timestamp: int):
        l = self.store[key]
        left = 0
        right = len(l) - 1
        result = ''
        while left <= right:
            middle = (left+right) // 2
            if l[middle][0] <= timestamp:
                result = l[middle][1]
                left = middle + 1
            else:
                right = middle - 1
        return result

    def _insert_sorted(self, l: List[Tuple[int, str]], t: Tuple[int, str]):
        '''
        This implementation of sorted insertion is equivalent to:
        from bisect import insort_left
        insort_left(l, t)
        '''
        left = 0
        right = len(l)
        while left < right:
            middle = (left + right) // 2
            if l[middle] < t:
                left = middle + 1
            else:
                right = middle
        l.insert(left, t)

