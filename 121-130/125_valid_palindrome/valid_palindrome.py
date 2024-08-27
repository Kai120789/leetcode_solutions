class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return True

        s = s.lower()
        s = ''.join(s)
        s = ''.join(c for c in s if c.isalpha() or c.isalnum())
        s1 = s[0:len(s)/2]
        if len(s) % 2 == 1:
            s2 = s[(len(s)/2+1):]
        else:
            s2 = s[(len(s)/2):]
        s2 = s2[::-1]

        print(s, s1, s2)

        if s1 == s2:
            return True
        else:
            return False