class Solution:
    def trap(self, nums: List[int]) -> int:
        n=len(nums)
        pref=[0]*(n)
        suff=[0]*(n)
        pref[0]=nums[0]
        ans=0
        suff[n-1]=nums[n-1]
        for i in range(n):
            pref[i]=max(pref[i-1],nums[i])
        for i in range(n-2,-1,-1):
            suff[i]=max(suff[i+1],nums[i])
        for i in range(n):
            ans+=(min(pref[i],suff[i])-nums[i])
        return ans