class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap={}
        hmap1={}
        for i in s:
            hmap[i]=hmap.get(i,0)+1
        for j in t:
            hmap1[j]=hmap1.get(j,0)+1
        if hmap1==hmap:
            return True
        else:
            return False