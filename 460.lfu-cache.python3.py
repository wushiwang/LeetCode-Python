#
# [460] LFU Cache
#
# https://leetcode.com/problems/lfu-cache/description/
#
# algorithms
# Hard (25.58%)
# Total Accepted:    23.2K
# Total Submissions: 90.7K
# Testcase Example:  '["LFUCache","put","put","get","put","get","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]'
#
# Design and implement a data structure for Least Frequently Used (LFU) cache.
# It should support the following operations: get and put.
#
#
#
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reaches its capacity, it should invalidate the least
# frequently used item before inserting a new item. For the purpose of this
# problem, when there is a tie (i.e., two or more keys that have the same
# frequency), the least recently used key would be evicted.
#
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LFUCache cache = new LFUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.get(3);       // returns 3.
# cache.put(4, 4);    // evicts key 1.
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
#
# LRU + 432
# Hashtable + Doubly linked list


class LFUCache:

    class DList:

        class DListNode:
            def __init__(self, val):
                self.val = val
                self.next = None
                self.pre = None

        def __init__(self):
            self.head = None
            self.tail = None

        def add(self, node, val):
            nn = self.DListNode(val)
            if node is None:
                if self.head is None:
                    self.head = self.tail = nn
                else:
                    nn.next = self.head
                    self.head.pre = nn
                    self.head = nn
            else:
                tmp = node.next
                node.next = nn
                nn.pre = node
                nn.next = tmp
                if tmp is not None:
                    tmp.pre = nn
                else:
                    self.tail = nn

        def delete(self, node):
            pre, nxt = node.pre, node.next
            if pre is not None:
                pre.next = nxt
            else:
                self.head = nxt
            if nxt is not None:
                nxt.pre = pre
            else:
                self.tail = pre

        def print(self):
            tmp = self.head
            res = ''
            while tmp is not None:
                res += str(tmp.val) + ': '
                tmp2 = tmp.keys.head
                while tmp2 is not None:
                    res += str(tmp2.val) + ', '
                    tmp2 = tmp2.next
                res += ' | '
                tmp = tmp.next
            print(res)

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.flist = self.DList()
        # key -> (fnode, rnode)
        self.dic = dict()
        self.val = dict()
        self.capacity = capacity
        self.size = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            fnode, rnode = self.dic[key]
            fre = fnode.val
            if fnode.next is None or fnode.next.val != fre+1:
                self.flist.add(fnode, fre+1)
                fnode.next.keys = self.DList()
                fnode.next.keys.add(None, key)
            else:
                fnode.next.keys.add(fnode.next.keys.tail, key)
            self.dic[key] = (fnode.next, fnode.next.keys.tail)
            fnode.keys.delete(rnode)
            if fnode.keys.head is None:
                self.flist.delete(fnode)
            return self.val[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return
        if key not in self.dic:
            if self.size != self.capacity:
                if self.flist.head is None or self.flist.head.val != 0:
                    self.flist.add(None, 0)
                    self.flist.head.keys = self.DList()
                    self.flist.head.keys.add(None, key)
                else:
                    self.flist.head.keys.add(self.flist.head.keys.tail, key)
                self.size += 1
            else:
                # Delete 1
                dkey = self.flist.head.keys.head.val
                #print(key, dkey)
                self.flist.head.keys.delete(self.flist.head.keys.head)
                if self.flist.head.keys.head is None:
                    self.flist.delete(self.flist.head)
                self.dic.pop(dkey)
                self.val.pop(dkey)
                # Add
                if self.flist.head is None or self.flist.head.val != 0:
                    self.flist.add(None, 0)
                    self.flist.head.keys = self.DList()
                    self.flist.head.keys.add(None, key)
                else:
                    self.flist.head.keys.add(self.flist.head.keys.tail, key)
            self.dic[key] = (self.flist.head, self.flist.head.keys.tail)
            self.val[key] = value
        else:
            fnode, rnode = self.dic[key]
            fre = fnode.val
            if fnode.next is None or fnode.next.val != fre+1:
                self.flist.add(fnode, fre+1)
                fnode.next.keys = self.DList()
                fnode.next.keys.add(None, key)
            else:
                fnode.next.keys.add(fnode.next.keys.tail, key)
            self.dic[key] = (fnode.next, fnode.next.keys.tail)
            self.val[key] = value
            fnode.keys.delete(rnode)
            if fnode.keys.head is None:
                self.flist.delete(fnode)
        #self.flist.print()
        return


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
