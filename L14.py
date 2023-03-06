class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        letter = str()
        for i in zip(*strs):
            if len(set(i)) == 1:
                letter += i[0]
            else:
                return letter
        return letter    
       
a = Solution()
strs = ["flower","flow","flight"]
print(a.longestCommonPrefix(strs))        