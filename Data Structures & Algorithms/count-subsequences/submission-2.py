class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = defaultdict(list)
        res = [0] * len(t)
        for i in range(len(t)):
            memo[t[i]].append(i)
        print(memo)
        for i in range(len(s)):
            # memo at 1 - number of distinct subsequences containing the string 'c'
            # memo at 2 - number of distinct subsequences containing the string 'ca'
            # memo at 3 - number of distinct subsequences containing the string 'cat'
            if s[i] in memo:
                for idx in memo[s[i]][-1::-1]:
                    if idx == 0:
                        res[idx] += 1
                    else:
                        res[idx] += res[idx-1]
                    print(res)
        return res[-1] 

