class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        list_n = list(str(n))

        print(list_n)
        count = 0
        while n != 1:
            list_n = list(str(n))
            n = 0
            for el in list_n:
                n += int(el) ** 2
            count += 1
            if count == 10:
                break

        print(n)
        return True if n == 1 else False