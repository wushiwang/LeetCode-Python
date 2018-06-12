#
# [148] Sort List
#
# https://leetcode.com/problems/sort-list/description/
#
# algorithms
# Medium (30.34%)
# Total Accepted:    136.8K
# Total Submissions: 449.3K
# Testcase Example:  '[4,2,1,3]'
#
# Sort a linked list in O(n log n) time using constant space complexity.
#
# Example 1:
#
#
# Input: 4->2->1->3
# Output: 1->2->3->4
#
#
# Example 2:
#
#
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sz, tmp = 0, head
        while tmp:
            sz, tmp = sz+1, tmp.next
        return self.mergeSort(head, sz)

    def mergeSort(self, head, size):
        if size == 0:
            return
        if size == 1:
            head.next = None
            return head
        pos, mid, i = head, size//2, 0
        while i != mid:
            pos, i = pos.next, i+1
        return self.merge(self.mergeSort(head, i),
                          self.mergeSort(pos, size-i))

    def merge(self, l1, l2):
        # Make sure size of l1 and l2 >= 1, and l1.val <= l2.val
        if l1.val > l2.val:
            l1, l2 = l2, l1
        pre, c1, c2 = l1, l1.next, l2
        while not (c1 is None and c2 is None):
            if c1 is None:
                pre.next = c2
                return l1
            elif c2 is None:
                return l1
            else:
                if c1.val <= c2.val:
                    pre, c1 = pre.next, c1.next
                else:
                    cur = c2
                    c2 = c2.next
                    pre.next = cur
                    cur.next = c1
                    pre = pre.next
        return l1
