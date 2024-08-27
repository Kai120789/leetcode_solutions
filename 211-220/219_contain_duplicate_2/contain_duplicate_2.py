class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) == len(set(nums)):
            return False
        i = 0
        while i < len(nums):
            j = 0
            while j < len(nums):
                if i != j and nums[i] == nums[j] and abs(i-j) <= k:
                    return True
                j += 1
            i += 1