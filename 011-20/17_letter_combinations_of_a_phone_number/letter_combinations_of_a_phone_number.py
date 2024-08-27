class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        proizvd = 3 ** (len(digits) - digits.count('9') - digits.count('7'))
        if digits.count('9') > 0:
            proizvd *= 4 ** digits.count('9')
        if digits.count('7') > 0:
            proizvd *= 4 ** digits.count('7')
        print(proizvd)
        nums = '23456789'
        var = ('abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz')
        # заполняем res, первый раз просто проходясь и добавляя каждую первую букву длина массива / длину строки вар для первой буквы раз, к каждой строке прибавляем буквы в 3 или 4 раза чаще в зависимости об длины строки вар
        res = []
        half_res = []
        count = 0
        for i in range(count, len(digits)):
            count2 = 0
            proizvd //= len(var[nums.index(digits[count])])
            while count2 < len(var[nums.index(digits[count])]):
                count3 = 0
                for k in range(count3, proizvd):
                    if count == 0:
                        res.append(var[nums.index(digits[count])][count2])
                    else:
                        half_res.append(var[nums.index(digits[count])][count2])
                    count3 += 1
                count2 += 1
                if half_res and len(res) != len(half_res) and count2 == len(var[nums.index(digits[count])]):
                    count2 = 0
            if half_res:
                cnt = 0
                while cnt < len(res):
                    res[cnt] += half_res[cnt]
                    cnt += 1
                half_res = []
            count += 1

        print(res)

        return res