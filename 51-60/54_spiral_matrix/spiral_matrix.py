class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        while matrix:
            j = 0
            while [] in matrix:
                if matrix[j] == []:
                    matrix.pop(j)
                else:
                    j += 1
            if matrix:
                for el in matrix[0]:
                    res.append(el)
                matrix.pop(0)
            for i in range(0, len(matrix)):
                res.append(matrix[i][-1])
                matrix[i].pop(-1)
            j = 0
            while [] in matrix:
                if matrix[j] == []:
                    matrix.pop(j)
                else:
                    j += 1
            if matrix:
                for el in matrix[-1][::-1]:
                    res.append(el)
                matrix.pop(-1)
            for i in range(1, len(matrix)+1):
                res.append(matrix[-i][0])
                matrix[-i].pop(0)
        print(res)
        return res