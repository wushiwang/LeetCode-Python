#
# [160] Intersection of Two Linked Lists
#
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
#
# algorithms
# Easy (30.81%)
# Total Accepted:    199K
# Total Submissions: 645.7K
# Testcase Example:  'No intersection: []\n[]'
#
# Write a program to find the node at which the intersection of two singly
# linked lists begins.
#
# For example, the following two linked lists:
#
# A:          a1 → a2
# ⁠                  ↘
# ⁠                    c1 → c2 → c3
# ⁠                  ↗
# B:     b1 → b2 → b3
#
# begin to intersect at node c1.
#
# Notes:
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function
# returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
#
#
#
# Credits:Special thanks to @stellari for adding this problem and creating all
# test cases.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # First pass: get length of two lists
        L1, L2, h1, h2 = 0, 0, headA, headB
        while h1:
            L1 += 1
            h1 = h1.next
        while h2:
            L2 += 1
            h2 = h2.next

        # Start at same point
        if L1 < L2:
            headA, headB, L1, L2 = headB, headA, L2, L1
        gap = L1 - L2
        for _ in range(gap):
            headA = headA.next
        while headA:
            if headA == headB:
                return headA
            headA, headB = headA.next, headB.next

        return
