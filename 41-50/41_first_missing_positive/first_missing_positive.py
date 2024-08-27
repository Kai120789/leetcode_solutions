class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums2 = sorted(nums)
        start = 1
        for el in nums2:
            if el == start:
                start += 1
            if el > start:
                return start
        return start