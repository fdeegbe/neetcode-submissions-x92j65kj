class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sidx = 0
        tidx = 0
        while tidx < len(t):
            while sidx < len(s) and s[sidx] != t[tidx]:
                print(s[sidx], t[tidx])
                sidx += 1
            if sidx >= len(s):
                break
            tidx += 1
            sidx += 1
        return len(t) - tidx
