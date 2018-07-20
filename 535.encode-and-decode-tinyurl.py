#
# [535] Encode and Decode TinyURL
#
# https://leetcode.com/problems/encode-and-decode-tinyurl/description/
#
# algorithms
# Medium (74.07%)
# Total Accepted:    44.7K
# Total Submissions: 60.4K
# Testcase Example:  '"https://leetcode.com/problems/design-tinyurl"'
#
# Note: This is a companion problem to the System Design problem: Design
# TinyURL.
#
# TinyURL is a URL shortening service where you enter a URL such as
# https://leetcode.com/problems/design-tinyurl and it returns a short URL such
# as http://tinyurl.com/4e9iAk.
#
# Design the encode and decode methods for the TinyURL service. There is no
# restriction on how your encode/decode algorithm should work. You just need to
# ensure that a URL can be encoded to a tiny URL and the tiny URL can be
# decoded to the original URL.
#


class Codec:
    def __init__(self):
        self.cnt = 0
        self.dic = dict()

    def encode(self, longUrl):
        """
        Encodes a URL to a shortened URL.
        :type longUrl: str
        :rtype: str
        """
        short = "http://nmh.com/" + str(self.cnt)
        self.dic[str(self.cnt)] = longUrl
        self.cnt += 1
        return short

    def decode(self, shortUrl):
        """
        Decodes a shortened URL to its original URL.
        :type shortUrl: str
        :rtype: str
        """
        n = shortUrl.split('/')[-1]
        return self.dic[n]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
