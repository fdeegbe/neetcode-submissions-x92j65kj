class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for word in words:
            for challenger in words:
                if word == challenger:
                    continue
                if word in challenger and word not in res:
                    res.append(word)
        return res