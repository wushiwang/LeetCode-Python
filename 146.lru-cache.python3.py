#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Hard (20.23%)
# Total Accepted:    180.3K
# Total Submissions: 888.1K
# Testcase Example:  '["LRUCache","put","put","get","put",
#                      "get","put","get","get","get"]\n
#                     [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
#
# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
#
#
#
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.
#
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
#


class LRUCache:
    class DListNode:
        """
        Doubly linked list Node
        """
        def __init__(self, val=None):
            self.val = val
            self.pre = None
            self.nxt = None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.dic = dict()
        self.head = None
        self.tail = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # Update doubly linked list
        if key not in self.dic:
            return -1
        res = self.dic[key]
        if self.size != 1:
            if self.head == res:
                self.head = res.nxt
                self.tail.nxt, res.pre, res.nxt = res, self.tail, None
                self.tail = res
            elif self.tail != res:
                res.pre.nxt, res.nxt.pre = res.nxt, res.pre
                self.tail.nxt, res.pre, res.nxt = res, self.tail, None
                self.tail = res
        return res.val[1]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dic:
            self.dic[key].val = (key, value)
            self.get(key)
        else:
            node = self.DListNode((key, value))
            # Insert new node to doubly linked list
            if self.size < self.capacity and key not in self.dic:
                if self.size == 0:
                    self.head = node
                else:
                    self.tail.nxt, node.pre = node, self.tail
                self.size += 1
            # Set least recently node to new value
            else:
                # Delete least recently value from dic
                self.dic.pop(self.head.val[0])
                self.head = self.head.nxt
                self.tail.nxt, node.pre = node, self.tail
            self.tail = node
            self.dic[key] = node
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
