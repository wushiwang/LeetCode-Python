#
# [432] All O`one Data Structure
#
# https://leetcode.com/problems/all-oone-data-structure/description/
#
# algorithms
# Hard (27.89%)
# Total Accepted:    10.5K
# Total Submissions: 37.6K
# Testcase Example:  '["AllOne","getMaxKey","getMinKey"]\n[[],[],[]]'
#
# Implement a data structure supporting the following operations:
#
#
#
# Inc(Key) - Inserts a new key  with value 1. Or increments an existing key by
# 1. Key is guaranteed to be a non-empty string.
# Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise
# decrements an existing key by 1. If the key does not exist, this function
# does nothing. Key is guaranteed to be a non-empty string.
# GetMaxKey() - Returns one of the keys with maximal value. If no element
# exists, return an empty string "".
# GetMinKey() - Returns one of the keys with minimal value. If no element
# exists, return an empty string "".
#
#
#
#
# Challenge: Perform all these in O(1) time complexity.
#


class AllOne:
    class List:
        class DListNode:
            def __init__(self, val):
                self.val = val
                self.keys = set()
                self.next = None
                self.pre = None

        def __init__(self):
            self.head = None
            self.tail = None

        def remove(self, node):
            if node.next is not None and node.pre is not None:
                node.pre.next = node.next
                node.next.pre = node.pre
                node.pre = node.next = None
            elif node.next is None:
                node.pre.next = None
                self.tail = node.pre
                node.pre = None
            elif node.pre is None:
                node.next.pre = None
                self.head = node.next
                node.next = None

        def add(self, node, val, key):
            nn = self.DListNode(val)
            nn.keys.add(key)
            if node is None: # Head
                if self.head is None:
                    self.head = self.tail = nn
                else:
                    nn.next = self.head
                    self.head.pre = nn
                    self.head = nn
            else:
                tmp = node.next
                if tmp is None:
                    node.next = nn
                    nn.pre = node
                    self.tail = nn
                else:
                    node.next = nn
                    nn.pre = node
                    nn.next = tmp
                    tmp.pre = nn
            return nn

        def print(self):
            tmp = self.head
            while tmp:
                print(tmp.val, tmp.keys)
                tmp = tmp.next
            print(self.head.val, self.tail.val)
            print("...")

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = self.List()
        self.dic = dict()

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key not in self.dic:
            if self.list.head is None or self.list.head.val != 1:
                self.list.add(None, 1, key)
            else:
                self.list.head.keys.add(key)
            self.dic[key] = self.list.head
        else:
            node = self.dic[key]
            node.keys.remove(key)
            if node.next is None or node.next.val != node.val+1:
                self.dic[key] = self.list.add(node, node.val+1, key)
            else:
                node.next.keys.add(key)
                self.dic[key] = node.next
            if len(node.keys) == 0:
                self.list.remove(node)

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.dic:
            node = self.dic[key]
            node.keys.remove(key)
            if node.val == 1:
                self.dic.pop(key)
            elif node.pre is None:
                self.dic[key] = self.list.add(None, node.val-1, key)
            elif node.pre.val != node.val-1:
                self.dic[key] = self.list.add(node.pre, node.val-1, key)
            else:
                node.pre.keys.add(key)
                self.dic[key] = node.pre
            if len(node.keys) == 0:
                self.list.remove(node)


    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.list.tail is None:
            return ""
        return next(iter(self.list.tail.keys))

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.list.head is None:
            return ""
        return next(iter(self.list.head.keys))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
