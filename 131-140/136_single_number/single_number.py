class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while True:
            num = nums[0]
            nums.remove(num)
            if num not in nums:
                return num
            else:
                while num in nums:
                    nums.remove(num)