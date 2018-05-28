#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (32.05%)
# Total Accepted:    128K
# Total Submissions: 399.3K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes in
# the end should remain as it is.
#
#
#
#
# Example:
#
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
#
# Note:
#
#
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be
# changed.
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1:
            return head

        dum = ListNode(-1)
        dum.next = head
        root = dum

        slow, fast, i = root.next, root, 0
        while i != k:
            fast = fast.next
            if fast is None:
                return dum.next
            i = i + 1

        while True:
            self.reverse(slow, fast, root)
            fast, root = slow, slow
            slow, i = slow.next, 0
            while i != k:
                fast = fast.next
                if fast is None:
                    return dum.next
                i = i + 1
        return dum.next

    def reverse(self, L, R, root):
        """
        reverse linked-list between node L and R
        """
        end = R.next
        cur = L
        while L.next != end:
            root.next = L.next
            tmp = L.next.next
            root.next.next = cur
            cur = root.next
            L.next = tmp
