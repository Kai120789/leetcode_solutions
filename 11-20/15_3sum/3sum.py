class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        half_res = set()
        nums.sort()
        for i in range(0, len(nums) - 1):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                summ = nums[i] + nums[left] + nums[right]
                if summ == 0:
                    half_res.add((nums[i], nums[left], nums[right]))
                    right -= 1
                    left += 1
                elif summ > 0:
                    right -= 1
                else:
                    left += 1
        for elem in half_res:
            res.append(list(elem))

        return res