class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        k = 1
        while count < n-1:
            if(count == 0):
                z = k
                k += 1
                k_old = z
            else:
                z = k
                k += k_old
                k_old = z
            count += 1
        return k