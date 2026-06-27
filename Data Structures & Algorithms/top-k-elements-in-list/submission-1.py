class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap={}
        for i in nums:
            hmap[i]=hmap.get(i,0)+1
        a=[]
        for i in hmap:
            a.append([hmap[i],i])
        a.sort()
        res=[]
        for i in range(k):
            tup=a.pop()
            res.append(tup[1])
        return res