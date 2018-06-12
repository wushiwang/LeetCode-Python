#
# [142] Linked List Cycle II
#
# https://leetcode.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (30.43%)
# Total Accepted:    152.1K
# Total Submissions: 500.4K
# Testcase Example:  '[]\nno cycle'
#
#
# Given a linked list, return the node where the cycle begins. If there is no
# cycle, return null.
#
#
#
# Note: Do not modify the linked list.
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
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return
        back = slow = fast = head
        flag = False
        while fast is not None and fast.next is not None:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                flag = True
                break
        if not flag:
            return
        L, R = back, slow
        while L != R:
            L = L.next
            R = R.next
        return L
