class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1m = Counter(s1)
        s2m = Counter(s2[:len(s1)])
        print(s1m, s2m)
        for i in range(0,(len(s2) - len(s1))):
            if s1m == s2m:
                return True

            if s2m[s2[i]] == 1:
                del s2m[s2[i]]
            else:
                s2m[s2[i]] -= 1

            s2m[s2[len(s1)+i]] = s2m.get(s2[len(s1)+i], 0) + 1
            print(s2m)
        if s1m == s2m:
            return True
        else:
            return False



        