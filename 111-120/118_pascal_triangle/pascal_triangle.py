class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        count1 = 1
        while count1 <= numRows:
            count2 = 0
            half_res = []
            while count2 < count1:
                if count1 == 1:
                    half_res.append(1)
                elif count2 == 0 or count2 == count1-1:
                    half_res.append(1)
                else:
                    half_res.append(res[count1-2][count2] + res[count1-2][count2-1])
                count2 += 1
            res.append(half_res)
            count1 += 1

        return res