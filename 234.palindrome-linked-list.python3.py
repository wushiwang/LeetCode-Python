#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (33.72%)
# Total Accepted:    168K
# Total Submissions: 498K
# Testcase Example:  '[1,2]'
#
# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
#
# Input: 1->2
# Output: false
#
# Example 2:
#
#
# Input: 1->2->2->1
# Output: true
#
# Follow up:
# Could you do it in O(n) time and O(1) space?
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        slow, fast, dum = head, head, ListNode(None)
        dum.next = head
        while fast is not None and fast.next is not None:
            slow, fast = slow.next, fast.next.next
            dum = dum.next
        # Reverse right half of linked list
        if fast is None:
            pre, cur = dum, dum.next
        else:
            pre, cur = slow, slow.next
        while cur.next:
            tmp1, tmp2 = pre.next, cur.next
            pre.next = cur.next
            cur.next = cur.next.next
            tmp2.next = tmp1
        # Check palindrom
        if fast is None:
            L, R = head, dum.next
        else:
            L, R = head, slow.next
        while R:
            if L.val != R.val:
                return False
            L, R = L.next, R.next
        return True
