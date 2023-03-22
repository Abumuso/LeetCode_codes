class Solution:
    def diagonalSum(self, mat: list) -> int:
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i==j:
                    count+=mat[i][j]
            count+=mat[i][len(mat[i])-i-1]    
        if len(mat[i])%2==1:
            count-=mat[len(mat)//2][len(mat)//2]        
        return(count)            

c = Solution()
mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]] 
print(c.diagonalSum(mat))      