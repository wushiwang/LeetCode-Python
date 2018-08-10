#
# [850] Insert into a Cyclic Sorted List
#
# https://leetcode.com/problems/insert-into-a-cyclic-sorted-list/description/
#
# algorithms
# Medium (14.34%)
# Total Accepted:    1.2K
# Total Submissions: 8.4K
# Testcase Example:  '{"$id":"1","next":{"$id":"2","next":{"$id":"3","next":{"$ref":"1"},"val":3},"val":3},"val":3}\n0'
#
# Given a node from a cyclic linked list which is sorted in ascending order,
# write a function to insert a value into the list such that it remains a
# cyclic sorted list. The given node can be a reference to any single node in
# the list, and may not be necessarily the smallest value in the cyclic list.
#
# If there are multiple suitable places for insertion, you may choose any place
# to insert the new value. After the insertion, the cyclic list should remain
# sorted.
#
# If the list is empty (i.e., given node is null), you should create a new
# single cyclic list and return the reference to that single node. Otherwise,
# you should return the original given node.
#
# The following example may help you understand the problem better:
#
#
#
#
#
# In the figure above, there is a cyclic sorted list of three elements. You are
# given a reference to the node with value 3, and we need to insert 2 into the
# list.
#
#
#
#
#
#
#
#
#
# The new node should insert between node 1 and node 3. After the insertion,
# the list should look like this, and we should still return node 3.
#
#
#
#
#
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if head is None:
            node = Node(insertVal, None)
            node.next = node
            return node
        maxx, minn = head.val, head.val
        tmp = head.next
        while tmp != head:
            maxx, minn = max(maxx, tmp.val), min(minn, tmp.val)
            tmp = tmp.next
        ret = head
        if insertVal > maxx:
            while True:
                if head.val == maxx:
                    node = Node(insertVal, head.next)
                    head.next = node
                    return ret
                head = head.next
        elif insertVal < minn:
            while True:
                if head.next.val == minn:
                    node = Node(insertVal, head.next)
                    head.next = node
                    return ret
                head = head.next
        else:
            while True:
                if insertVal >= head.val and insertVal <= head.next.val:
                    node = Node(insertVal, head.next)
                    head.next = node
                    return ret
                head = head.next
