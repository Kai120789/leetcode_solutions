class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        left = 0
        right = len(height) - 1
        while right > left:
            most = (right - left) * height[right] if height[right] < height[left] else (right - left) * height[left]
            if most > res:
                res = most

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return res