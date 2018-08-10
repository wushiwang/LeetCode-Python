#
# [838] Design Linked List
#
# https://leetcode.com/problems/design-linked-list/description/
#
# algorithms
# Easy (12.89%)
# Total Accepted:    3.3K
# Total Submissions: 25.4K
# Testcase Example:  '["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]\n[[],[1],[3],[1,2],[1],[1],[1]]'
#
# Design your implementation of the linked list. You can choose to use the
# singly linked list or the doubly linked list. A node in a singly linked list
# should have two attributes: val and next. val is the value of the current
# node, and next is a pointer/reference to the next node. If you want to use
# the doubly linked list, you will need one more attribute prev to indicate the
# previous node in the linked list. Assume all nodes in the linked list are
# 0-indexed.
#
# Implement these functions in your linked list class:
#
#
# get(index) : Get the value of the index-th node in the linked list. If the
# index is invalid, return -1.
# addAtHead(val) : Add a node of value val before the first element of the
# linked list. After the insertion, the new node will be the first node of the
# linked list.
# addAtTail(val) : Append a node of value val to the last element of the linked
# list.
# addAtIndex(index, val) : Add a node of value val before the index-th node in
# the linked list. If index equals to the length of linked list, the node will
# be appended to the end of linked list. If index is greater than the length,
# the node will not be inserted.
# deleteAtIndex(index) : Delete the index-th node in the linked list, if the
# index is valid.
#
#
# Example:
#
#
# MyLinkedList linkedList = new MyLinkedList();
# linkedList.addAtHead(1);
# linkedList.addAtTail(3);
# linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
# linkedList.get(1);            // returns 2
# linkedList.deleteAtIndex(1);  // now the linked list is 1->3
# linkedList.get(1);            // returns 3
#
#
# Note:
#
#
# All values will be in the range of [1, 1000].
# The number of operations will be in the range of [1, 1000].
# Please do not use the built-in LinkedList library.
#

def myprint(func):
    def wrapper(self, *args, **argv):
        ret = func(self, *args, **argv)
        """
        node = self.head
        res = func.__name__ + str(args)
        while node is not None:
            res += str(node.val) + ' '
            node = node.next
        res += ': ' + str(self.size)
        print(res)
        """
        return ret
    return wrapper


class MyLinkedList:
    class ListNode:
        def __init__(self, val):
            self.next = None
            self.val = val

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0

    @myprint
    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index > self.size-1:
            return -1
        pos, node = 0, self.head
        while pos < index and node is not None:
            node = node.next
            pos += 1
        if node is None or pos != index:
            return -1
        else:
            return node.val

    @myprint
    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = self.ListNode(val)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    @myprint
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        node = self.ListNode(val)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    @myprint
    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        pos, node, nnode = 0, self.head, self.ListNode(val)

        if index == 0:
            self.addAtHead(val)
            return
        elif index == self.size:
            self.addAtTail(val)
            return
        elif index > self.size or index < 0:
            return

        while pos < index -1 and node is not None:
            node = node.next
            pos += 1
        if pos == index - 1 and node is not None:
            nnode.next = node.next
            node.next = nnode
            self.size += 1

    @myprint
    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        pos, node = 0, self.head
        if index == 0:
            if self.head.next is None:
                self.head = self.tail = None
            else:
                self.head = self.head.next
            self.size -= 1
            return
        elif index == self.size -1:
            if self.head == self.tail:
                self.head = self.tail = None
                self.size -= 1
                return
        elif index >= self.size or index < 0:
            return

        while pos < index - 1 and node is not None:
            node = node.next
            pos += 1
        if pos == index - 1 and node is not None:
            node.next = node.next.next
            if node.next is None:
                self.tail = node
            self.size -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
