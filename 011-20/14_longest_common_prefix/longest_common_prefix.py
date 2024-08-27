class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        count = 0
        prefs = []
        while count <= len(strs[0]):
            prefs.append(strs[0][0:count])
            count += 1

        ind = 0
        srez = 0
        while ind < len(prefs):
            count = 0
            while count < len(strs):

                if (prefs[ind] == strs[count][0:srez]):
                    count += 1
                else:
                    return prefs[ind - 1]

            srez += 1
            ind += 1

        

        if(len(strs) > 1):
            return prefs[ind-1]
        else:
            return strs[0]