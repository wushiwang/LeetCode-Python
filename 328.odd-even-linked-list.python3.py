#
# [328] Odd Even Linked List
#
# https://leetcode.com/problems/odd-even-linked-list/description/
#
# algorithms
# Medium (45.39%)
# Total Accepted:    100.4K
# Total Submissions: 221.1K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given a singly linked list, group all odd nodes together followed by the even
# nodes. Please note here we are talking about the node number and not the
# value in the nodes.
#
# You should try to do it in place. The program should run in O(1) space
# complexity and O(nodes) time complexity.
#
# Example 1:
#
#
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
#
#
# Example 2:
#
#
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL
#
#
# Note:
#
#
# The relative order inside both the even and odd groups should remain as it
# was in the input.
# The first node is considered odd, the second node even and so on ...
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        back, tail, cnt = head, head, 0
        while tail.next:
            tail = tail.next
            cnt += 1
        cnt += 1
        if cnt == 2:
            return head
        cnt, cur = cnt >> 1, 0
        while cur != cnt:
            tmp = head.next
            head.next = head.next.next
            tail.next = tmp
            tmp.next = None
            head, tail = head.next, tail.next
            cur += 1
        return back
