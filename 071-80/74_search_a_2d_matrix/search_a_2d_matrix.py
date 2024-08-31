class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i, el in enumerate(matrix):
            if el[-1] >= target:
                if target in matrix[i]:
                    return True
                else:
                    return False