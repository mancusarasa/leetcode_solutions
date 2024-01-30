#!/usr/bin/env python3
from .time_based_key_value_store import TimeMap


class TestTimeBasedKeyValueStore:
    def test_case_one(self):
        obj = TimeMap()
        obj.set('foo', 'bar', 1)
        assert obj.get('foo', 1) == 'bar'
        assert obj.get('foo', 3) == 'bar'
        obj.set('foo', 'bar2', 4)
        assert obj.get('foo', 4) == 'bar2'
        assert obj.get('foo', 5) == 'bar2'
