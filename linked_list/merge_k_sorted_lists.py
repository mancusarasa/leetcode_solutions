#!/usr/bin/env python3
'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []
'''
from math import inf
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0:
            return None
        elif k == 1:
            return lists[0]
        else:
            result_head = None
            result_tail = None
            all_lists_are_empty = False
            while not all_lists_are_empty:
                next_node = lists[0]
                next_node_index = 0
                for index, node in enumerate(lists):
                    if next_node is None:
                        next_node = node
                        next_node_index = index
                    elif node is not None and node.val < next_node.val:
                        next_node = node
                        next_node_index = index
                if next_node is None:
                    all_lists_are_empty = True
                else:
                    next_value = next_node.val
                    new_node = ListNode(next_value)
                    lists[next_node_index] = lists[next_node_index].next
                    if result_head is None:
                        result_head = new_node
                        result_tail = new_node
                    else:
                        result_tail.next = new_node
                        result_tail = new_node
            return result_head
