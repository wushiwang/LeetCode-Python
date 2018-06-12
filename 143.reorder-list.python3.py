#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list/description/
#
# algorithms
# Medium (27.10%)
# Total Accepted:    114.6K
# Total Submissions: 422K
# Testcase Example:  '[1,2,3,4]'
#
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
#
# Example 1:
#
#
# Given 1->2->3->4, reorder it to 1->4->2->3.
#
# Example 2:
#
#
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        # Find the middle point of list using tow-pointer algorithm
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow, fast = slow.next, fast.next.next

        # Reverse right-half list
        if slow.next is not None:
            L = slow.next
            while L.next is not None:
                tmp = L.next.next
                L.next.next = slow.next
                slow.next = L.next
                L.next = tmp

        # Merge left and right half lists
        L, R = head, slow.next
        slow.next = None
        while R is not None:
            tmp = R.next
            R.next = L.next
            L.next = R
            R = tmp
            L = L.next.next
        return
