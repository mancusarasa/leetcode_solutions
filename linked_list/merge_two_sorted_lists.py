#!/usr/bin/env python3

'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        # both lists have elements
        head_one = list1
        head_two = list2
        merged_list = None
        # pick the first element of the result
        first_element = min(head_one.val, head_two.val)
        # manually advance the first pointer to reflect that
        # the min is already added to the result
        if head_one.val < head_two.val:
            head_one = head_one.next
        else:
            head_two = head_two.next
        merged_list = ListNode(first_element, None)
        result_iterator = merged_list
        while (head_one is not None) or (head_two is not None):
            if head_one is None:
                new_node = ListNode(head_two.val, None)
                head_two = head_two.next
                result_iterator.next = new_node
                result_iterator = result_iterator.next
            elif head_two is None:
                new_node = ListNode(head_one.val, None)
                head_one = head_one.next
                result_iterator.next = new_node
                result_iterator = result_iterator.next
            else:
                min_element = min(head_one.val, head_two.val)
                if head_one.val < head_two.val:
                    head_one = head_one.next
                else:
                    head_two = head_two.next
                new_node = ListNode(min_element, None)
                result_iterator.next = new_node
                result_iterator = result_iterator.next

        return merged_list
