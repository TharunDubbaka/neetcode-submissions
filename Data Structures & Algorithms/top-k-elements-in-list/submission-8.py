import heapq as hp

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap={}
        for i in nums:
            hmap[i]=hmap.get(i,0)+1
        heap=[]
        vals=[]
        for idx,value in hmap.items():
            heapq.heappush(heap,(value,idx))
            if len(heap)>k:
                hp.heappop(heap)
        for i in heap:
            vals.append(i[1])
        return vals