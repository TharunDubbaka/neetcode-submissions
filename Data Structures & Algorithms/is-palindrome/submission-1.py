class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        l=0
        r=n-1
        def alnum(a):
            return (ord('a')<=ord(a)<=ord('z') or ord('A')<=ord(a)<=ord('Z') or ord('0') <= ord(a)<=ord('9'))
        while l<r:
            while l<r and not alnum(s[l]):
                l+=1
            while r>l and not alnum(s[r]):
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True

