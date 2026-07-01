class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        sett = set()
        for i in range(len(t)):
            if s[i] in mapping :
                if mapping[s[i]] != t[i]:
                    return False
            else:
                if t[i] in sett:
                    return False
                mapping[s[i]] = t[i]
                sett.add(t[i])
        return True