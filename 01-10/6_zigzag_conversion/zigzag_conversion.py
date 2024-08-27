class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        f = True
        chars = []
        for i in range(0, numRows):
            chars.append('')

        count = 0
        for char in s:
            chars[count] += char
            if count < numRows-1 and f:
                count += 1
            else:
                count -= 1
                f = False

            if count == 0:
                f = True
        res = ''
        for elem in chars:
            res += elem
        
        return (res)