class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t = sorted(t)
        s = sorted(s)
        return s == t
        