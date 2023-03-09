class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = list()
        for i in s.split(" "):
            if i.isalnum():
                lst.append(i) 
        return len(lst[-1])          
          

a = Solution()
s = "   fly me   to   the moonbn  "
print(a.lengthOfLastWord(s))        