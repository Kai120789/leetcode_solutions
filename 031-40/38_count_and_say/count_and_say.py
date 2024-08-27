class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        start = '1'
        for z in range(len(start), n):
            hr = ''
            res = []
            for el in start:
                if el not in hr:
                    if hr:
                        res.append(hr)
                        hr = ''
                    hr += el
                else:
                    hr += el
            res.append(hr)
            start = ''
            for elem in res:
                start += str(len(elem)) + elem[0]
            print(start)
        return start