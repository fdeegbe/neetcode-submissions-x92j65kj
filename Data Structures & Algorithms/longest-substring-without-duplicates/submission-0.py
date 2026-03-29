class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = maxlen = 0
        n = len(s)
        red = set()

        while j < n:
            if s[j] not in red:
                red.add(s[j])
                maxlen = max(maxlen, len(red))
            else:
                # print(red)
                while s[j] in red:
                    # print(s[i])
                    red.remove(s[i])
                    i+=1
                red.add(s[j])
            j+=1

        return maxlen

        