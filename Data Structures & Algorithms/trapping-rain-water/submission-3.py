class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        prefm=[0]*(n)
        prefm[0]=height[0]
        sufm=[0]*(n)
        sufm[n-1]=height[n-1]
        ans=0
        for i in range(1,n):
            prefm[i]=max(prefm[i-1],height[i])
        for i in range(n-2,-1,-1):
            sufm[i]=max(sufm[i+1],height[i])
        #print(prefm,sufm)
        for i in range(n):
            ans+=(min(prefm[i],sufm[i])-height[i])
        return ans
