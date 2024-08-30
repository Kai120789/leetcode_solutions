class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) < 2:
            return [nums]

        lenght = 1
        count = len(nums)
        while count > 0:
            lenght *= count
            count -= 1
        print(lenght)

        count = 0
        for i in range(0, len(nums)):
            for j in range(0, lenght // len(nums)):
                res.append([nums[count]])
            count += 1

        if len(nums) == 6:
            numbers = [30, 120, 360]
            for s in range(0, 3):
                count = 0
                for i in range(0, numbers[s]): # 720 // 24 = 30
                    for k in range(0, len(nums)):
                        if count < lenght and nums[k] not in res[count]:
                            for j in range(0, lenght // numbers[s]):
                                res[count].append(nums[k])
                                count += 1

        if len(nums) == 5:
            numbers = [20, 60]
            for s in range(0, 2):
                count = 0
                for i in range(0, numbers[s]): # 720 // 24 = 30
                    for k in range(0, len(nums)):
                        if count < lenght and nums[k] not in res[count]:
                            for j in range(0, lenght // numbers[s]):
                                res[count].append(nums[k])
                                count += 1

        if len(nums) == 4:
            numbers = [10]
            for s in range(0, 1):
                count = 0
                for i in range(0, numbers[s]): # 720 // 24 = 30
                    for k in range(0, len(nums)):
                        if count < lenght and nums[k] not in res[count]:
                            for j in range(0, lenght // numbers[s]):
                                res[count].append(nums[k])
                                count += 1

        print(res)

        z2 = 0
        while z2 < 2:
            count = 0
            for i in range(0, lenght):
                j = 0
                while j < len(nums):
                    if count < lenght and nums[j] not in res[count] and res[count] + [nums[j]] not in res:
                        res[count].append(nums[j])
                        count += 1
                        break
                    j += 1
            z2 += 1

        return res