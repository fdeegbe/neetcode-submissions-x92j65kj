class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        res = 0
        for c in s:
            for j in range(i,len(t)):
                if c == t[j]:
                    res += 1
                    i = j+1
                    break
                if j == len(t)-1:
                    return False
        return True if res == len(s) else False