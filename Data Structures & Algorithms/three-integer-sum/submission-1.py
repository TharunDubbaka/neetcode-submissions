class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        for i,a in enumerate(nums):
            if i>0 and nums[i-1]==nums[i]:
                continue
            l,r=i+1,n-1
            while l<r:
                tripsum=a+nums[l]+nums[r]
                if tripsum==0:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                    #r-=1
                elif tripsum>0:
                    r-=1
                else:
                    l+=1
        return res
        
            

            
        # a+b+c=target
        # a+b = target-c