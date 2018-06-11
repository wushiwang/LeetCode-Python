#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (25.78%)
# Total Accepted:    160.3K
# Total Submissions: 621.9K
# Testcase Example:  '{}'
#
#
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
#
#
#
# Return a deep copy of the list.
#
#
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dic, root = dict(), RandomListNode(-1)
        dum, back = root, head
        while head is not None:
            root.next = RandomListNode(head.label)
            dic[head] = root.next
            root, head = root.next, head.next
        root, head = dum.next, back
        while head is not None:
            root.random = dic[head.random] if head.random is not None else None
            root, head = root.next, head.next
        return dum.next
