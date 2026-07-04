class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hm1={}
        hm2={}
        l1=len(s1)
        l2=len(s2)
        for i in s1:
            hm1[i]=hm1.get(i,0)+1
        for ch in s2[:l1]:
            hm2[ch]=hm2.get(ch,0)+1
        if hm1==hm2:
            return True
        i=0
        for j in range(l1,l2):
            hm2[s2[j]]=hm2.get(s2[j],0)+1
            hm2[s2[i]]-=1
            if hm2[s2[i]]==0:
                del hm2[s2[i]]
            i+=1
            if hm1==hm2:
                return True
        return False