class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack=[]
        stack2=[]
        for i in range(len(s)):
            if s[i]=="(":
                stack.append("(")
            else:
                if stack:
                    stack.pop()
                else:
                    stack2.append(")")

        return len(stack)+len(stack2)