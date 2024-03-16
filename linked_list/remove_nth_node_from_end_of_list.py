'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

'''
#!/usr/bin/env python3
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        previous = None
        p1 = head
        p2 = head
        for _ in range(n):
            p2 = p2.next
        while p2 is not None:
            previous = p1
            p1 = p1.next
            p2 = p2.next
        if p1 == head:
            return head.next
        previous.next = p1.next if p1 else None
        return head
