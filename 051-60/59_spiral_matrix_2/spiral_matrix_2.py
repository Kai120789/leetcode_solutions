class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(0, n):
            hr = []
            for j in range(0, n):
                hr.append(0)
            res.append(hr)
        print(res)
        nums = list(range(1, n ** 2 + 1))
        check = 0
        while nums:
            for i in range(check, n-check):
                res[check][i] = nums[0]
                nums.pop(0)
            for j in range(1+check, n-check):
                res[j][-1 - check] = nums[0]
                nums.pop(0)
            for i in range(n - 2 - check, -1 + check, -1):
                res[-1 - check][i] = nums[0]
                nums.pop(0)
            for j in range(n - 2 - check, check, -1):
                res[j][check] = nums[0]
                nums.pop(0)
            check += 1
        print(res)
        return res