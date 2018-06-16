#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (33.74%)
# Total Accepted:    159.3K
# Total Submissions: 472K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Remove all elements from a linked list of integers that have value val.
#
# Example:
#
#
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dum = ListNode(None)
        dum.next = head
        pre = dum
        while head:
            if head.val == val:
                pre.next = head.next
                head = head.next
            else:
                pre, head = pre.next, head.next
        return dum.next
