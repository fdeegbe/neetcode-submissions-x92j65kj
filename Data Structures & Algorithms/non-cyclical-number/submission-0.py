class Solution:
    def isHappy(self, n: int) -> bool:
        check = set()
        q = []
        print(str(n).split())
        while n not in q:
            res = 0
            q.append(n)
            for i in str(n):
                res += int(i) *int(i)
            print(res)
            n = res
            if res == 1:
                return True
        return False
        