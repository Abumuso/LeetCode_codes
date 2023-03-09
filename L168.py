class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        res = str()
        while columnNumber > 0:
            b = columnNumber%26
            if b == 0:
                b=26
                columnNumber = (columnNumber//26)-1
            else:
                columnNumber = columnNumber//26    
            res = chr(b+64)+res
        return res              

c = Solution()
columnNumber = 701
print(c.convertToTitle(columnNumber))            
