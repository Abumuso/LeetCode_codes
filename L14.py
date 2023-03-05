class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        for i in range(len(strs)):
            for j in range(len(i)):
                


a = Solution()
strs = strs = ["flower","flow","flight"]
print(a.longestCommonPrefix(strs))        