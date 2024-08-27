class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [1000, 100, 10, 1]
        res = list(str(num))
        str_res = ''
        if len(values) == len(res):
            str_res += 'M' * int(res[0])
            num -= values[0] * int(res[0])
            res.pop(0)

        if num > 99:
            if num < 400:
                str_res += 'C' * int(res[0])
                num -= values[1] * int(res[0])
            elif num < 500:
                str_res += 'CD'
                num -= 400
            elif num < 900:
                str_res += 'D'
                num -= 500
                str_res += 'C' * (int(res[0]) - 5)
                num -= values[1] * (int(res[0]) - 5)
            else:
                str_res += 'CM'
                num -= 900
                
            res.pop(0) 

        if int(res[0]) == 0:
            res.pop(0)

        if num > 9:
            if num < 40:
                str_res += 'X' * int(res[0])
                num -= values[2] * int(res[0])
            elif num < 50:
                str_res += 'XL'
                num -= 40
            elif num < 90:
                str_res += 'L'
                num -= 50
                str_res += 'X' * (int(res[0]) - 5)
                num -= values[2] * (int(res[0]) - 5)
            else:
                str_res += 'XC'
                num -= 90
            res.pop(0)
            
        if num < 10:
            if num < 4:
                str_res += 'I' * num
                num -= values[3] * num
            elif num < 5:
                str_res += 'IV'
                num -= 4
            elif num < 9:
                str_res += 'V'
                num -= 5
                str_res += 'I' * (num)
                num -= values[3] * (num)
            else:
                str_res += 'IX'
                num -= 9
            res.pop(0)
        
        return str_res