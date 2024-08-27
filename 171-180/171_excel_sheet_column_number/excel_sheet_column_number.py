class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        str_ex = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        n = len(columnTitle)
        pows = []

        while len(pows) != len(columnTitle):
            pows.append(str_ex.index(columnTitle[n-1]))
            n -= 1

        print(pows)
        count = 0
        summa = 0
        n = len(columnTitle)

        while count < len(columnTitle):
            summa += 26 ** (n-1) * pows[n-1]
            count += 1
            n -= 1

        print(summa)
        return summa