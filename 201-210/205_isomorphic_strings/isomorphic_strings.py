class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        count = 0
        s1 = []
        t1 = []
        s2 = []
        t2 = []
        while count < len(s):
            if s[count] not in s2 and t[count] not in t2:
                s1.append(count)
                s2.append(s[count])
                t1.append(count)
                t2.append(t[count])
            elif s[count] in s2 and t[count] in t2:
                s1.append(s.index(s[count]))
                t1.append(t.index(t[count]))
            else:
                return False
            count += 1
        print(s1, t1)
        return True if s1 == t1 else False