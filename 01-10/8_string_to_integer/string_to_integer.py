class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = ''
        nums = '0123456789'
        s = s.strip()

        if not s or s == '-':
            return 0

        if s[0] == '-':
            res = res + '-'
            s = s[1:]
        
        if s[0] == '+' and '-' not in res:
            s = s[1:]

        

        for num in s:
            if num in nums:
                res = res + num
            else: 
                break

        print(res)

        if res and res != '-' and int(res) < -2 ** 31:
            return -2 ** 31
        
        if res and res != '-' and int(res) > 2 ** 31 - 1:
            return 2 ** 31 - 1

        if res == '-':
            return 0

        return 0 if not res else int(res)