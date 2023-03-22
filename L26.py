class Solution:
    def removeDuplicates(self, nums: list) -> int:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)-1):
                if nums[i]==nums[j]:
                    nums.remove(nums[j]) 
        return(nums)            


c = Solution()    
nums = [0,0,1,1,1,2,2,3,3,4]
print(c.removeDuplicates(nums))