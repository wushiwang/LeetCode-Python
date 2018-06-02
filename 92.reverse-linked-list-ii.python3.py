#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (31.66%)
# Total Accepted:    141.6K
# Total Submissions: 447.2K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Reverse a linked list from position m to n. Do it in one-pass.
#
# Note: 1 ≤ m ≤ n ≤ length of list.
#
# Example:
#
#
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
#


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dum = ListNode(-1)
        dum.next, i = head, 0
        pre = dum

        while head is not None:
            i += 1
            if i == m:
                for _ in range(n-m):
                    tmp = head.next.next
                    head.next.next = pre.next
                    pre.next = head.next
                    head.next = tmp
                return dum.next
            head, pre = head.next, pre.next
