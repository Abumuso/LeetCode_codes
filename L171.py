class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num,n = 0,0
        for i in columnTitle[::1]:
            n += ord(i) - 64
            num = n
            n*=26
        return num


c = Solution()
columnTitle = "AAA"
print(c.titleToNumber(columnTitle))        