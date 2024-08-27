class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for el in nums:
            if nums.count(el) == 1:
                return el