#
# [445] Add Two Numbers II
#
# https://leetcode.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (46.68%)
# Total Accepted:    54.4K
# Total Submissions: 116.7K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The most significant digit comes first and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the
# lists is not allowed.
#
#
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sta1, sta2 = [], []
        while l1:
            sta1.append(l1.val)
            l1 = l1.next
        while l2:
            sta2.append(l2.val)
            l2 = l2.next
        add, res = 0, ListNode(None)
        while len(sta1) != 0 or len(sta2) != 0:
            s = add
            if len(sta1) != 0:
                s += sta1.pop()
            if len(sta2) != 0:
                s += sta2.pop()
            if s >= 10:
                s -= 10
                add = 1
            else:
                add = 0
            tmp = res.next
            res.next = ListNode(s)
            res.next.next = tmp
        if add == 1:
            tmp = res.next
            res.next = ListNode(1)
            res.next.next = tmp
        return res.next
