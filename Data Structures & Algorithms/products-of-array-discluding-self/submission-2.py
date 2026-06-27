class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefprod = []
        sufprod = [1]*len(nums)
        prefprod.append(1)
        for i in range(1,len(nums)):
            an=prefprod[i-1]*nums[i-1]
            prefprod.append(an)
        sufprod[len(nums)-1]=1
        for i in range(len(nums)-2, -1, -1):
            ab=sufprod[i+1]*nums[i+1]
            sufprod[i]=ab
        res=[]
        for i in range(len(nums)):
            res.append(sufprod[i]*prefprod[i])
        return res