class Solution:
    def partition(self, s: str) -> List[List[str]]:
        subset = []
        res = []


        def backtrack(i):
            if i == len(s):
                res.append(subset[::])
                return
            k = i
            for j in range(i, len(s)+1):
                if s[i:j][::-1] == s[i:j] and s[i:j]:
                    subset.append(s[i:j])
                    backtrack(j)
                    subset.pop()
            
        backtrack(0)
        return res
