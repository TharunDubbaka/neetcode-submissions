class Solution:
    def findMin(self, nums: List[int]) -> int:
        res=float('inf')
        l=0
        r=len(nums)-1
        while(l<=r):
            if nums[l]<=nums[r]:
                res=min(res,nums[l])
                break
            m=(l+r)//2
            if nums[l]<=nums[m]:
                res=min(res,nums[l])
                l=m+1
            else:
                r=m-1
                res=min(res,nums[m])
        return res
                