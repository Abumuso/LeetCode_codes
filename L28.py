class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
            

c = Solution()
haystack = "sadbutsad"
needle = "sad"
print(c.strStr(haystack, needle))
