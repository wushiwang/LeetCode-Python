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


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Log(k) times call mergeTwoLists
        if len(lists) == 0:
            return []
        if len(lists) == 1:
            return lists[0]

        return self.mergeTwoLists(self.mergeKLists(lists[:len(lists)//2]),
                                  self.mergeKLists(lists[len(lists)//2:]))

    def mergeTwoLists(self, a, b):
        """
        Merge two list, cost O(len(a)+len(b))
        """
        root = ListNode(-1)
        res = root
        while a is not None and b is not None:
            if a.val < b.val:
                res.next = a
                a, res = a.next, res.next
            else:
                res.next = b
                b, res = b.next, res.next

        if a is not None:
            res.next = a
        if b is not None:
            res.next = b
        return root.next
