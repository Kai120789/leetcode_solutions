class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        str_ex = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        res = ''
        my_pow = 0
        pows = []
        f = True
        
        if columnNumber <= 52:
            if columnNumber > 26:
                pows.append('A')
                columnNumber -= 26
            if columnNumber <= 26:
                pows.append(str_ex[columnNumber-1])
                res = ''.join(pows)
                print(res)
                return res

        if columnNumber % 26 != 0:
            ost = columnNumber % 26
            columnNumber -= ost
        else:
            ost = 26
            columnNumber -= ost


        while 26 ** my_pow < columnNumber:
            my_pow += 1

        if 26 ** my_pow >= columnNumber:
            my_pow -= 1



        while columnNumber and my_pow >= 0:
            count = 0
            while columnNumber - (26 ** my_pow) >= 0 and count < 26 and f:
                if count == 25 and columnNumber == 26 ** my_pow:
                    count += 1
                    columnNumber -= (26 ** my_pow)

                elif count == 25 and columnNumber - 26 == 0:
                    columnNumber -= (26 ** my_pow)
                    f = False
                elif columnNumber == 26 ** my_pow and columnNumber != 26:
                    
                    f = False
                else:
                    count += 1
                    columnNumber -= (26 ** my_pow)
            my_pow -= 1
            if(count != 0):
                pows.append(count)
            f = True

        if ost != 0: pows.append(ost)

        print(pows)
        for elem in pows:
            res += str_ex[elem - 1]
        print(res)
        
        return res