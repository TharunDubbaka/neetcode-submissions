class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        n=len(nums)
        j=n-1
        while i<j:
            mid=(i+j)//2
            # print(mid)
            if nums[mid]>nums[j]:
                i=mid+1
            else:
                j=mid
        start=i
        i,r = 0, n-1
        if target>=nums[start] and target<=nums[r]:
            i = start
        else:
            r=start-1
        while i<=r:
            mid=(i+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                i=mid+1
            else:
                r=mid-1
        return -1

        


