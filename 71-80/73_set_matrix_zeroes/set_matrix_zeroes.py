class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for j in range(0, len(matrix)):
            if 0 in matrix[j]:
                for i in range(0, len(matrix[j])):
                    if matrix[j][i] != 0:
                        matrix[j][i] = 2 ** 31

        zeros = []

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0:
                    zeros.append(j)

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if j in zeros:
                    matrix[i][j] = 0

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 2**31:
                    matrix[i][j] = 0