class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}

        for word in strs:
            new = "".join(sorted(word))
            if new in m:
                m[new].append(word)
            else:
                m[new] = [word]
        
        return m.values()
        