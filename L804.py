class Solution:
    def uniqueMorseRepresentations(self, words: list):
        lst = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        uniq = set()
        for i in words:
            a = str()
            for j in i:
                a+=lst[ord(j)-97]
            uniq.add(a)  
        return len(uniq)      


words = ["gin","zen","gig","msg"]
c = Solution()
print(c.uniqueMorseRepresentations(words))        