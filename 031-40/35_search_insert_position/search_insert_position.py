class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        count = 0
        while count < len(nums):
            if(nums[count] < target):
                count += 1
            else:
                return count

        return count