class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        for word in words:
            for challenger in words:
                if word == challenger:
                    continue
                if word in challenger:
                    res.add(word)
        return list(res)