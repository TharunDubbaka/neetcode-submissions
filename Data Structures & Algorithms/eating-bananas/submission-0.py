import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def bananas(arr,val):
            ans=0
            for i in arr:
                ans+=math.ceil(i/val)
            return ans
        i=1
        j=max(piles)
        minval=float('inf')
        while i<=j:
            mid=(i+j)//2
            ans=bananas(piles,mid)
            if ans>h:
                i=mid+1
            else:
                j=mid-1
                minval=min(minval,mid)
        return minval
            