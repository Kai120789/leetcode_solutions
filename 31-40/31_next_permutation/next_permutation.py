class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if nums == sorted(nums)[::-1]:
            nums += sorted(nums)
            for z in range(0, len(nums)//2):
                nums.pop(0)
            print(nums)
            return
        count = len(nums) - 1
        for i in range(count, 0, -1):
            if count != 0 and nums[count] > nums[count - 1]:
                part_nums = nums[0:count-1]
                second_part_nums = nums[count-1:]
                print(part_nums, second_part_nums)
                sort_nums = sorted(second_part_nums)[::-1]
                print(sort_nums[sort_nums.index(nums[count-1]) - 1])
                second_part_nums.remove(sort_nums[sort_nums.index(nums[count-1]) - 1])
                res = part_nums + [sort_nums[sort_nums.index(nums[count-1]) - 1]] + sorted(second_part_nums)
                nums += res
                for x in range(0, len(nums) // 2):
                    nums.pop(0)
                print(nums)
                return
            count -= 1