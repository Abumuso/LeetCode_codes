class Solution(object):
    def isPalindrome(self, s):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a=str()
        for i in s:
            if i.isalnum():
                a+=i
        a=a.lower()
        if a == a[::-1]:
            return True
        return False
    
ob = Solution()        
s = "race a car"
print(ob.isPalindrome(s))