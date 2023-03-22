class Solution:
    def singleNumber(self, nums: list):
        for i in nums:
            if nums.count(i)==1:
                return i

c=Solution()
nums = [4,1,2,1,2]
print(c.singleNumber(nums))