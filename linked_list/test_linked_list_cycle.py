from .linked_list_cycle import ListNode, Solution


class TestLinkedListCycle:
    def test_linked_list_with_cycle_returns_true(self):
        head = ListNode(3)
        head.next = ListNode(2)
        head.next.next = ListNode(0)
        head.next.next.next = ListNode(4)
        head.next.next.next = head.next
        s = Solution()
        assert s.hasCycle(head) == True

    def test_linked_list_no_cycles_returns_false(self):
        head = ListNode(3)
        head.next = ListNode(4)
        head.next.next = ListNode(5)
        s = Solution()
        assert s.hasCycle(head) == False

    def test_single_loop_returns_true(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = head
        s = Solution()
        assert s.hasCycle(head) == True
