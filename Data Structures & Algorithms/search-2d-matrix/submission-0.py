class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        found = False
        m,n=len(matrix[0]),len(matrix)
        row,col=0,n-1
        while row<=col:
            lst=(row+col)//2
            if target>(matrix[lst][-1]):
                row=lst+1
            elif target<(matrix[lst][0]):
                col=lst-1
            else:
                break
        if not (row<=col):
            return False
        lst=(row+col)//2
        l,r=0,m-1
        while l<=r:
            m=(l+r)//2
            if target>matrix[lst][m]:
                l=m+1
            elif target<matrix[lst][m]:
                r=m-1
            else:
                return True
        return False