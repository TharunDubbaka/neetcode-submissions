import heapq as hp

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap={}
        for i in nums:
            hmap[i]=hmap.get(i,0)+1
        vals=[]
        val=[]
        for idx,value in hmap.items():
            val.append((value,idx))
            
        arr=sorted(val)
        print(arr)
        for i in range(k):
            vals.append(arr.pop()[1])
        return vals