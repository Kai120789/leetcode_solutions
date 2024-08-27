class Solution:
    def mySqrt(self, x: int) -> int:
        if(x == 0 or x == 1):
            return x
        
        count = 1
        while count < x * x:
            if (x < count * count):
                return count-1
            elif(x == count * count):
                return count
            else:
                count += 1