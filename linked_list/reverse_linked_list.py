#!/usr/bin/env python3
'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]
'''

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        new_head = ListNode(head.val, None)
        next_node = None
        pointer = head.next
        while pointer is not None:
            new_node = ListNode(pointer.val, new_head)
            new_head = new_node
            pointer = pointer.next
        return new_head
