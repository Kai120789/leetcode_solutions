class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [-1, -1] if target not in nums else [nums.index(target), nums.index(target) + nums.count(target) - 1]