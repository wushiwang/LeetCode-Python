#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (28.60%)
# Total Accepted:    229K
# Total Submissions: 800.2K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
#
# Example:
#
#
# Input:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# Output: 1->1->2->3->4->4->5->6
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
import math


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ListNode.__lt__ = lambda self, other: self.val < other.val

        lists = list(filter(lambda x: x is not None, lists))

        if len(lists) == 0:
            return []

        if len(lists) == 1:
            return lists[0]

        heapq.heapify(lists)

        root = ListNode(-1)
        cur, res = heapq.heappop(lists), root
        while True:
            res.next = cur
            if cur.next is not None:
                heapq.heappush(lists, cur.next)
            if len(lists) == 0:
                break
            cur, res = heapq.heappop(lists), res.next

        return root.next
