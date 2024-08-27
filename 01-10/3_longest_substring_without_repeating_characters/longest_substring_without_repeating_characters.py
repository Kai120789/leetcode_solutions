class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       
        count = 0
        res = 0
        res_max = 0
        chars = []
        while count < len(s) :
            if (s[count] not in chars):
                chars.append(s[count])
                count += 1
                res += 1
            else:
                if res > res_max:
                    res_max = res
                else:
                    res_max = res_max
                chars = []
                count = count - res + 1
                res = 0

        return res if res > res_max else res_max