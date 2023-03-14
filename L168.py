class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        # res = str()
        # while columnNumber > 0:
        #     b = columnNumber%26
        #     if b == 0:
        #         b=26
        #         columnNumber = (columnNumber//26)-1
        #     else:
        #         columnNumber = columnNumber//26    
        #     res = chr(b+64)+res
        # return res   
        res = str()
        if columnNumber < 27:
            res = chr(columnNumber+64)
        else:
            res = chr(columnNumber//26+64) + c.convertToTitle(columnNumber//26)
        return res[::-1]

c = Solution()
columnNumber = 54
print(c.convertToTitle(columnNumber))  
       
