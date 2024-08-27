class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        count = 0
        res = []
        for i in range(0, len(s) - len(words[0]) * len(words) + 1):
            substrings = [s[z+count:len(words[0])+z+count] for z in range(0, len(words)*len(words[0]), len(words[0]))]

            if sorted(words) == sorted(substrings):
                res.append(i)
            count += 1
        return res