#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (33.84%)
# Total Accepted:    125.7K
# Total Submissions: 371.4K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given a linked list and a value x, partition it such that all nodes less than
# x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the
# two partitions.
#
# Example:
#
#
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dum, A, B = ListNode(-1), ListNode(-1), ListNode(-1)
        dum.next = head
        dumA, dumB = A, B

        while head is not None:
            if head.val < x:
                A.next = head
                A = A.next
            else:
                B.next = head
                B = B.next

            head = head.next

        if dumA.next is None:
            return dumB.next
        if dumB.next is None:
            return dumA.next

        B.next = None
        A.next = dumB.next
        return dumA.next
