#
# [71] Simplify Path
#
# https://leetcode.com/problems/simplify-path/description/
#
# algorithms
# Medium (26.47%)
# Total Accepted:    115K
# Total Submissions: 434.2K
# Testcase Example:  '"/home/"'
#
# Given an absolute path for a file (Unix-style), simplify it.
#
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
#
# Corner Cases:
#
#
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together,
# such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".
#


class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        res = list()
        for p in path.split('/'):
            if p == '':
                if len(res) == 0:
                    res.append('')
            elif p == '.':
                pass
            elif p == '..':
                if len(res) != 1:
                    res = res[:-1]
            else:
                res.append(p)
        if len(res) == 1:
            return "/"
        return '/'.join(res)
