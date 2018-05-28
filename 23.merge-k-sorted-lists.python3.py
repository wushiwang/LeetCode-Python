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

        if len(lists) == 0:
            return []

        if len(lists) == 1:
            return lists[0]

        for i in range(len(lists)):
            if lists[i] is None:
                lists[i] = ListNode(math.inf)
        heapq.heapify(lists)

        root = ListNode(-1)
        cur, res = heapq.heappop(lists), root
        while cur.val != math.inf:
            res.next = cur
            if cur.next is None:
                heapq.heappush(lists, ListNode(math.inf))
            else:
                heapq.heappush(lists, cur.next)
            cur, res = heapq.heappop(lists), res.next

        return root.next
