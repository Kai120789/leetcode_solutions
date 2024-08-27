class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if (len(a) < len(b)):
            while (len(a) != len(b)):
                a = '0' + a
        elif (len(b) < len(a)):
            while (len(a) != len(b)):
                b = '0' + b


        transit = 0
        c = []
        length = len(a) if len(a) >= len(b) else len(b)
        count = length - 1
        while count >= 0:
            if (a[count] == '1' and b[count] == '1'):
                if (transit == 0):
                    c.append('0')
                    transit = 1
                else:
                    c.append('1')
                    transit = 1
            elif (a[count] != b[count]):
                if (transit == 0):
                    c.append('1')
                    transit = 0
                else:
                    c.append('0')
                    transit = 1
            else:
                if (transit == 0):
                    c.append('0')
                    transit = 0
                else:
                    c.append('1')
                    transit = 0
            count -= 1
            if(count == -1 and transit == 1):
                c.append('1')

        k = 0
        end = len(c) - 1
        while k < end:
            c[k], c[end] = c[end], c[k]
            end -= 1
            k += 1

        s = ''.join(map(str, c))
        return s