class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefprod = []
        sufprod = [1]*len(nums)
        prefprod.append(1)
        for i in range(1,len(nums)):
            an=prefprod[i-1]*nums[i-1]
            prefprod.append(an)
        sufprod[len(nums)-1]=1
        for i in range(len(nums)-2,-1,-1):
            an=sufprod[i+1]*nums[i+1]
            #print(an)
            sufprod[i]=an
        res=[]
        for i in range(len(nums)):
            res.append(prefprod[i]*sufprod[i])
        return res
        