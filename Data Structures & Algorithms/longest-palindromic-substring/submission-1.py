class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = s
        s = '#' + '#'.join(s) + '#'
        print(s)
        dp = [0] * len(s)
        n = len(s)
        l,r = 0,0
        for i in range(n):
            dp[i] = min(r-i, dp[l + (r-l)]) if i < r else 0
            while (i + dp[i] + 1 < n and i - dp[i] - 1 >= 0 and s[i + dp[i] + 1] == s[i - dp[i] - 1]):
                    dp[i] += 1
            if i + dp[i] > r:
                l,r = i-dp[i], i+dp[i]
        resLen, centerIdx = max((v,i) for i,v in enumerate(dp))
        # print(resLen, centerIdx, dp,t, s[centerIdx-(resLen//2): centerIdx + (resLen//2)])
        resIdx = (centerIdx - resLen) // 2
        return t[resIdx: resIdx+resLen]


            
