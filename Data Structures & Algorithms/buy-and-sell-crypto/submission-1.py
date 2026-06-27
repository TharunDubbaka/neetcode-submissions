class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        l=0
        r=l+1
        prof =0
        while r<n:
            if prices[l]<prices[r]:
                prof=max(prof,prices[r]-prices[l])
            else:
                l = r
            r+=1
        return prof