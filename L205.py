class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        count = 0
        if s == t:
            return True
        else:
            for i in range(len(s)-1):
                for j in range(i+1,len(s)):
                    if s[i]==s[j]and t[i]==t[j]:
                            count += 1
            if count >= 1:
                return True
            return False           
s = "aaeaa"
t = "uuxyy"
c = Solution()
print(c.isIsomorphic(s,t))