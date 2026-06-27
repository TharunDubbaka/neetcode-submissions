class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zers=nums.count(0)
        n=len(nums)
        if zers>1:
            return [0]*(n)
        totmul=1
        for i in range(n):
            if nums[i]==0:
                continue
            else:
                totmul*=nums[i]
        res=[0]*n
        for i in range(n):
            if nums[i]==0:
                res=[0]*n
                res[i]=totmul
                return res
            else:
                res[i]=totmul//nums[i]
        return res
            