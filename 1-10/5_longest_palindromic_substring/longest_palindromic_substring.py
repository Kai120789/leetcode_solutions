class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        count1 = 0
        res = ''

        if s == s[::-1]:
            return s

        while count1 < len(s):
            s1 = s[count1:]
            count2 = count1 + 1
            while count2 < len(s)+1:
                s2 = s[count1:count2]
                if s2 == s2[::-1] and len(s2) > len(res):
                    res = s2
                count2 += 1
            count1 += 1

        return res