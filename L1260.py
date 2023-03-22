class Solution:
    def shiftGrid(self, grid: list, k: int):
        lst = list()
        for i in grid:
            for j in i:
                lst.append(j)
        a = int()       
        while(k>0):    
            a = lst.pop()
            lst.insert(0,a)
            k-=1
        z=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j]=lst[z]
                z+=1
        return grid        



c = Solution()
grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print(c.shiftGrid(grid,k))     