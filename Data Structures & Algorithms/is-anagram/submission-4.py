class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap1={}
        hmap2={}
        for i in s:
            hmap1[i]=hmap1.get(i,0)+1
        for j in t:
            hmap2[j]=hmap2.get(j,0)+1
        return hmap1==hmap2


