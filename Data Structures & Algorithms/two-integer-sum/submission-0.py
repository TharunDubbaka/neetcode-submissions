class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap={}
        for i,v in enumerate(nums):
            d=target - nums[i]
            if d in hmap:
                return [hmap[d], i]
            hmap[v]=i
         
