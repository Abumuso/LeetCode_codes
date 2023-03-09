class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return(bin(int(a,2)+int(b,2))[2:])

c=Solution()
a,b="11","1"
print(c.addBinary(a,b))