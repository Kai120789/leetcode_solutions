class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hp = set(nums)
        for el in hp:
            while nums.count(el) > 2:
                nums.remove(el)
        return len(nums)