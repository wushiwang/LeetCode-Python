#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (30.20%)
# Total Accepted:    137.2K
# Total Submissions: 454.4K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
#
# Example 1:
#
#
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
#
#
# Example 2:
#
#
# Input: 1->1->1->2->3
# Output: 2->3
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode(-1)
        pre.next = head
        dum = pre

        L, R = head, head
        while R is not None:
            while R.next is not None and R.next.val == R.val:
                R = R.next
            if L != R:
                pre.next = R.next
            else:
                pre.next = L
                pre = pre.next
            L, R = R.next, R.next

        return dum.next
