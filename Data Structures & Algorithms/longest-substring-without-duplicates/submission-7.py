class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap={}
        i=0
        n=len(s)
        if n==0:
            return 0
        j=0
        ml=0
        while j<n:
            hmap[s[j]]=hmap.get(s[j],0)+1
            while hmap[s[j]]>1:
                hmap[s[i]]-=1
                if hmap[s[i]]==0:
                    del hmap[s[i]]
                i+=1
            j+=1
            ml=max(ml,j-i+1)
        return ml-1

                
            