#
# [588] Design In-Memory File System
#
# https://leetcode.com/problems/design-in-memory-file-system/description/
#
# algorithms
# Hard (36.24%)
# Total Accepted:    2.9K
# Total Submissions: 8K
# Testcase Example:  '["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]\n[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]'
#
# Design an in-memory file system to simulate the following functions:
#
# ls: Given a path in string format. If it is a file path, return a list that
# only contains this file's name. If it is a directory path, return the list of
# file and directory names in this directory. Your output (file and directory
# names together) should in lexicographic order.
#
# mkdir: Given a directory path that does not exist, you should make a new
# directory according to the path. If the middle directories in the path don't
# exist either, you should create them as well. This function has void return
# type.
#
# addContentToFile: Given a file path and file content in string format. If the
# file doesn't exist, you need to create that file containing given content. If
# the file already exists, you need to append given content to original
# content. This function has void return type.
#
# readContentFromFile: Given a file path, return its content in string format.
#
# Example:
#
# Input:
# ["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
# [[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]
# Output:
# [null,[],null,null,["a"],"hello"]
# Explanation:
#
#
#
#
# Note:
#
# You can assume all file or directory paths are absolute paths which begin
# with / and do not end with / except that the path is just "/".
# You can assume that all operations will be passed valid parameters and users
# will not attempt to retrieve file content or list a directory or file that
# does not exist.
# You can assume that all directory names and file names only contain
# lower-case letters, and same names won't exist in the same directory.
#


class FileSystem:
    class Node:
        def __init__(self, name, t):
            self.name = name
            # 0: dir, 1: file
            self.t = t
            if t == 0:
                self.chd = dict()
            else:
                self.content = ""

    def __init__(self):
        self.root = self.Node('', 0)

    def _getNode(self, path, cur):
        if len(path) == 0:
            return cur
        return self._getNode(path[1:], cur.chd[path[0]])

    def _makeNode(self, path, cur):
        if len(path) == 0:
            return
        if path[0] not in cur.chd:
            node = self.Node(path[0], 0)
            cur.chd[path[0]] = node
        self._makeNode(path[1:], cur.chd[path[0]])

    def _makeFile(self, path, cur, content):
        if len(path) == 1:
            if path[0] not in cur.chd:
                f = self.Node(path[0], 1)
                f.content = content
                cur.chd[path[0]] = f
            else:
                cur.chd[path[0]].content += content
            return
        self._makeFile(path[1:], cur.chd[path[0]], content)

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        node = self._getNode(list(filter(lambda x: x != '', path.split('/'))), self.root)
        if node.t == 0:
            return sorted(list(node.chd))
        else:
            return [node.name]

    def mkdir(self, path):
        """
        :type path: str
        :rtype: void
        """
        self._makeNode(list(filter(lambda x: x != '', path.split('/'))), self.root)
        return

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: void
        """
        self._makeFile(list(filter(lambda x: x != '', filePath.split('/'))), self.root, content)

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        node = self._getNode(list(filter(lambda x: x != '', filePath.split('/'))), self.root)
        return node.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
