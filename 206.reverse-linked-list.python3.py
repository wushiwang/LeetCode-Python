#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (47.49%)
# Total Accepted:    364.3K
# Total Submissions: 766.2K
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
#
# Example:
#
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
#
#
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        dum = ListNode(None)
        dum.next = head
        while head.next:
            tmp, tmp2 = dum.next, head.next
            dum.next = head.next
            head.next = head.next.next
            tmp2.next = tmp
        return dum.next
