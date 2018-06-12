#
# [147] Insertion Sort List
#
# https://leetcode.com/problems/insertion-sort-list/description/
#
# algorithms
# Medium (34.14%)
# Total Accepted:    121.8K
# Total Submissions: 356.2K
# Testcase Example:  '[4,2,1,3]'
#
# Sort a linked list using insertion sort.
#
#
#
#
#
# A graphical example of insertion sort. The partial sorted list (black)
# initially contains only the first element in the list.
# With each iteration one element (red) is removed from the input data and
# inserted in-place into the sorted list
#
#
#
#
#
# Algorithm of Insertion Sort:
#
#
# Insertion sort iterates, consuming one input element each repetition, and
# growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data,
# finds the location it belongs within the sorted list, and inserts it
# there.
# It repeats until no input elements remain.
#
#
#
# Example 1:
#
#
# Input: 4->2->1->3
# Output: 1->2->3->4
#
#
# Example 2:
#
#
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        dum = ListNode(None)
        L = dum.next = head
        while L.next is not None:
            R = L.next
            if R.val >= L.val:
                L = L.next
                continue
            # Delete R from list
            L.next = R.next
            # Find insertion position
            pre, pos = dum, dum.next
            while True:
                if R.val <= pos.val:
                    pre.next = R
                    R.next = pos
                    break
                pre, pos = pre.next, pos.next
        return dum.next
