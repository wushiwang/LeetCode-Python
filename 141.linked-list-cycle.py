#
# [141] Linked List Cycle
#
# https://leetcode.com/problems/linked-list-cycle/description/
#
# algorithms
# Easy (34.99%)
# Total Accepted:    262.6K
# Total Submissions: 751.4K
# Testcase Example:  '[]\nno cycle'
#
#
# Given a linked list, determine if it has a cycle in it.
#
#
#
# Follow up:
# Can you solve it without using extra space?
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False
