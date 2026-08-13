class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        ml=0
        for i in nums:
            length=0
            if i-1 not in s:
                while i+length in s:
                    length+=1
                ml=max(length,ml)
        return ml