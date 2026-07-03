class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars=set()
        n=len(s)
        i=0
        j=0
        maxlen=0
        while i<n and j<n:
            #print(i,j,chars,maxlen)
            while s[j] in chars:
                chars.remove(s[i])
                i+=1
            chars.add(s[j])
            maxlen=max(maxlen,j-i+1)
            j+=1
        return maxlen
            