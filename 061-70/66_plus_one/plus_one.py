class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if (digits[-1] != 9):
            digits[-1] += 1
        else:
            k = 0
            for elem in digits:
                if elem != 9:
                    k += 1
            count = len(digits) - 1
            if (k == 0):
                digits.append(0)
            while digits[count] == 9:
                digits[count] = 0
                count -= 1
            if(k == 0):
                digits[count + 1] += 1
            else:
                digits[count] += 1

        return digits