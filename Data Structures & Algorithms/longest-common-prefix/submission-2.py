class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        res = strs[0]
        for word in strs[1:]:
            if not word:
                return ""
            for i in range(min(len(res),len(word))):
                if word[i] != res[i]:
                    res = res[:i]
                    break
        return res