class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        memo = { '}': '{',
        ']':'[',
        ')':'('}
        for c in s:
            if stack and stack[-1] == memo.get(c, None):
                stack.pop()
            else:
                stack.append(c)
        return not stack