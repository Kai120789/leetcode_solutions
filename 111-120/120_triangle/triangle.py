class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(0, len(triangle) - 1):
            if i == 0:
                triangle[1][0] += triangle[0][0]
                triangle[1][1] += triangle[0][0]
            else:
                triangle[1][0] += triangle[0][0]
                triangle[1][-1] += triangle[0][-1]
                for j in range(1, len(triangle[1]) - 1):
                    if triangle[0][j-1] >= triangle[0][j]:
                        triangle[1][j] += triangle[0][j]
                    else:
                        triangle[1][j] += triangle[0][j-1]
            triangle.pop(0)
            print(triangle)
        
        return min(triangle[0])