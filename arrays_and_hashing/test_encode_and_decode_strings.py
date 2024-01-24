#!/usr/bin/env python3

from .encode_and_decode_strings import Solution


class TestEncodeAndDecodeStrings:
    def test_one(self):
        self._assert_decode_encode_list_returns_original_list(["neet","code","love","you"])

    def test_two(self):
        self._assert_decode_encode_list_returns_original_list(["we","say",":","yes"])

    def _assert_decode_encode_list_returns_original_list(self, l):
        s = Solution()
        assert s.decode(s.encode(l)) == l
