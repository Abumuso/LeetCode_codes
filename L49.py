class Solution:
    def groupAnagrams(self, strs: list):
        lst = list()
        for i in range(len(strs)):
            count = 0
            for j in range(len(strs[i])):
                lst.append()
                if strs[i][j] in strs[i+1]:
                    count+=1

c=Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(c.groupAnagrams(strs))        