class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0
        check = []
        res = 0
        while count < len(s):
            if(s[count] == 'M' and ('c' in check) == False):
                res += 1000
            elif(s[count] == 'D'and ('c' in check) == False):
                res += 500
            elif(s[count] == 'C' and ('x' in check) == False):
                if(count == len(s)-1):
                    res += 100
                else:
                    if(s[count+1] == 'M'):
                        res += 900
                        check.append('c')
                    elif(s[count+1] == 'D'):
                        res += 400
                        check.append('c')
                    else:
                        res += 100
            elif(s[count] == 'L'and ('x' in check) == False):
                res += 50
            elif(s[count] == 'X' and ('i' in check) == False):
                if(count == len(s)-1):
                    res += 10
                else:
                    if(s[count+1] == 'C'):
                        res += 90
                        check.append('x')
                    elif(s[count+1] == 'L'):
                        res += 40
                        check.append('x')
                    else:
                        res += 10
            elif(s[count] == 'V' and ('i' in check) == False):
                res += 5
            elif(s[count] == 'I'):
                if(count == len(s)-1):
                    res += 1
                else:
                    if(s[count+1] == 'X'):
                        res += 9
                        check.append('i')
                    elif(s[count+1] == 'V'):
                        res += 4
                        check.append('i')
                    else:
                        res += 1
            count += 1
        return res