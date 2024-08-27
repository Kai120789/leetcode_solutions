class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        str_n = str(bin(n))[2:]
        res = 0
        while len(str_n) < 32:
            str_n = '0' + str_n
        l = len(str_n)
        while l > 0:
            if str_n[l-1] == '1':
                res += 2 ** (l-1)
            l -= 1

        print(res)
        return res