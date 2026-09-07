import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high=max(piles)
        low=1
        ans=float('inf')
        def currans(val):
            curr=0
            for i in piles:
                curr+=(math.ceil(i/val))
            return curr
        while low<=high:
            mid=(low+high)//2
            curr=currans(mid)
            if curr>h:
                low=mid+1
            else:
                ans=min(mid,ans)
                high=mid-1
        return ans
            



            