class Solution:
    def arrayStringsAreEqual(self, word1: list, word2: list):
        w = w2 = str()
        for i in word1:
            w += i
        for i in word2:    
            w2 += i
        if w == w2:
            return True
        return False    

c = Solution()
word1  = ["abc", "d", "defg"]
word2 = ["abcddefg"]
print(c.arrayStringsAreEqual(word1, word2))        