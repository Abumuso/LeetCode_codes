class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rim = ['I','V','X','L','C','D','M']
        arab = [1,5,10,50,100,500,1000]
        max = 0
        count = 0
        for i in range(len(s)):
            for j in range(len(rim)):
                if s[i] == rim[j]:
                    if max >= arab[j]:
                        max = arab[j]
                        count += max
                    else:
                        count -= max
                        max = arab[j] - max
                        count += max    
        return count            
            
a = Solution()
s = "MCMXCIV"
print(a.romanToInt(s))