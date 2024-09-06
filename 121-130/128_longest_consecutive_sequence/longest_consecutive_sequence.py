class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        nums = sorted(list(set(nums)))
        res = 0
        summa = 1
        for i in range(0, len(nums)-1):
            if nums[i + 1] - nums[i] == 1:
                summa += 1
            else:
                res = max(res, summa)
                summa = 1
        res = max(res, summa)
        print(res)
        return res