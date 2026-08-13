class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m=len(s)
        n=len(t)
        if m!=n:
            return False
        arr1=[0]*(27)
        arr2=[0]*(27)
        i=0
        while i<m:
            arr1[ord(s[i])-ord('a')]+=1
            arr2[ord(t[i])-ord('a')]+=1
            i+=1
        j=0
        #print(arr1,arr2)
        while j<27:
            #print(j)
            if arr1[j]!=arr2[j]:
                return False
            j+=1
        return True



