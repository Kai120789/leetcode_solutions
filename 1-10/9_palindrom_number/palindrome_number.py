class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0):
            return False
        else:
            x = list(str(x))
            y = []
            count = 0
            while count < len(x):
                y.append(x[len(x)-1-count])
                count+=1
            if x == y:
                return True
            else:
                return False
        