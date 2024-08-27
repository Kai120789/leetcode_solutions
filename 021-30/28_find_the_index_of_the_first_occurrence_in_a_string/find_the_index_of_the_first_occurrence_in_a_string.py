class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        str_count = 0
        count = 0
        k = 0
        while str_count < len(haystack):
            if (needle[count] == haystack[str_count]):
                if (count == 0):
                    k += 1
                str_count += 1
                count += 1
            else:
                if (count == 0):
                    k += 1
                str_count = k
                count = 0


            if (count == len(needle)):
                return str_count - len(needle)
        return -1