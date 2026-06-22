class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sidx = 0
        tidx = 0
        while tidx < len(t) and sidx < len(s):
            if s[sidx] == t[tidx]:
                tidx += 1
                sidx += 1
            else:
                sidx += 1
        
        return len(t) - tidx
