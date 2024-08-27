class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = s.split()
        m = m[::-1]
        res = ' '.join(m)
        return res