class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        strs = str()
        lst = ["(", ")", "[", "]", "{", "}"]
        for i in range(0,(len(s))-1,2):
            for j in range(0,(len(lst)),2):
                if s[i]==lst[j] and s[i+1]==lst[j+1]:
                    strs += s[i]+s[i+1]
                if s[i]==lst[j] and s[i+3]==lst[j+3] and s[i-2]==lst[j-2] or s[i+2]==lst[j+2]:
                # print(strs)            
        if strs == s:
            return True
        return False        


        
 
a = Solution()
s = "{[]}"        
print(a.isValid(s))
