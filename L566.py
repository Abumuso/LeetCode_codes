class Solution:
    def matrixReshape(self, mat: list, r: int, c: int):
        lst = list()
        if len(mat)*len(mat[0])!= r*c:
            return mat
        else:
            for i in range(len(mat)):
                for j in range(len(mat[i])):
                    print(mat[i][j])
            #         lst.append(mat[j])
            # print(lst)        


mat = [[1,2],[3,4]]
r = 1
c = 4
c = Solution()
print(c.matrixReshape(mat,r,c))