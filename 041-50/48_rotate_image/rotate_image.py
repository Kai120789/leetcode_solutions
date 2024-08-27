class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix2 = []
        for i in range(0, len(matrix[0])):
            hr = []
            for j in range(len(matrix)-1, -1, -1):
                hr.append(matrix[j][i])
            
            matrix2.append(hr)
        count = 0
        for m in matrix2:
            matrix.pop(0)
            matrix.append(matrix2[count])
            count += 1
        print(matrix2)
        return