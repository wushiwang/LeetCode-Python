#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (39.52%)
# Total Accepted:    217.8K
# Total Submissions: 551K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
#
# Example:
#
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Note:
#
#
# Your algorithm should use only constant extra space.
# You may not modify the values in the list's nodes, only nodes itself may be
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
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        root = ListNode(-1)
        root.next = head
        tmp = root
        slow, fast = head, head.next
        while True:
            slow.next = fast.next
            fast.next = slow
            tmp.next = fast
            slow, fast = fast, slow
            if fast.next is not None and fast.next.next is not None:
                slow, fast, tmp = slow.next.next, fast.next.next, fast
            else:
                break
        return root.next
