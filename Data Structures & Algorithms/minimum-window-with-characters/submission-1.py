class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sliding window - figure out the counts of the subrsting
        res = (-1,float('inf'))
        tgt = Counter(t) #target
        curr = {}
        print(tgt)
        l = r = 0
        while r < len(s):
            curr[s[r]] = curr.get(s[r], 0) + 1 # add it into the map
            # print(curr, len({k for k, v in tgt.items() if curr.get(k, 0) >= v}) == len(tgt))
            while len({k for k, v in tgt.items() if curr.get(k, 0) >= v}) == len(tgt):
                contender = sum(k[1] for k in curr.items())
                if res[1] > contender:
                    res = (l, contender)
                if curr[s[l]] == 1:
                    del curr[s[l]]
                else:
                    curr[s[l]] -= 1
                l+=1
                # print("match found ", tgt, curr, res)
            r+=1
        print(res)
        return s[res[0]:res[0]+res[1]] if res[0] != -1 else ""