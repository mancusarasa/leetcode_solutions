#!/usr/bin/env python3
from .remove_nth_node_from_end_of_list import ListNode, Solution


class TestRemoveNthFromEndOfList:
    def test_case_one(self):
        s = Solution()
        l = ListNode(1)
        l.next = ListNode(2)
        l.next.next = ListNode(3)
        l.next.next.next = ListNode(4)
        l.next.next.next.next = ListNode(5)
        s.removeNthFromEnd(l, 2)
        assert l.val == 1
        assert l.next.val == 2
        assert l.next.next.val == 3
        assert l.next.next.next.val == 5
        assert l.next.next.next.next is None

    def test_case_two(self):
        s = Solution()
        l = ListNode(1)
        h = s.removeNthFromEnd(l, 1)
        assert h is None

    def test_case_three(self):
        s = Solution()
        l = ListNode(1)
        l.next = ListNode(2)
        h = s.removeNthFromEnd(l, 1)
        assert h.val == 1
        assert h.next is None
