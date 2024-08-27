class Solution(object):
    def reverse(self, x):
        if x < 0:
            x *= (-1)
            str_x = str(x)
            str_x = str_x[::-1]
            return int(str_x) * -1 if int(str_x) < (2 ** 31 - 1) else 0
        else:
            str_x = str(x)
            str_x = str_x[::-1]
            return int(str_x) if int(str_x) < (2 ** 31 - 1) else 0