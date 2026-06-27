class Solution:
    def isValid(self, s: str) -> bool:
        mapping={"}":"{", "]":"[",")":"("}
        stack=[]
        for i in s:
            if i == "{" or i=="[" or i=="(":
                stack.append(i)
            elif i=="}" or i=="]" or i==")":
                if stack and stack[-1]==mapping[i]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False