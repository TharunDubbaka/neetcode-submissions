class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmaps={}
        hmapt={}
        for i in s:
            hmaps[i]=hmaps.get(i,0)+1
        for i in t:
            hmapt[i]=hmapt.get(i,0)+1
        if hmaps == hmapt:
            return True
        else:
            return False