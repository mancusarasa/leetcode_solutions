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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        iterator = head
        while iterator is not None:
            iterator = iterator.next
            length += 1
        index_to_remove = length - n
        if index_to_remove == 0:
            return head.next
        iterator = head
        for _ in range(index_to_remove-1):
            iterator = iterator.next
        iterator.next = None if iterator.next is None else iterator.next.next
        return head
