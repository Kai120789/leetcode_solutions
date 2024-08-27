class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        count = 0
        while count < len(nums):
            if(nums[count] == val):
                nums.pop(count)
            else:
                count += 1
        
        return len(nums)