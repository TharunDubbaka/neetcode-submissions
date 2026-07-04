class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        n=len(s)
        hm={}
        maxlen=0
        maxfreq=0
        while l<n and r<n:
            hm[s[r]]=hm.get(s[r],0)+1
            while ((r-l+1)-max(hm.values())>k):
                #print(hm,l,r)
                hm[s[l]]-=1
                l+=1
            r+=1
            maxlen=max(maxlen,r-l+1)
        return maxlen-1