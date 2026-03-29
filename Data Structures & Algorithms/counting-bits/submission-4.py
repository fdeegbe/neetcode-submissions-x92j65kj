class Solution:
    def countBits(self, n: int) -> List[int]:
        if n < 1:
            return [0]
        res = [0] * (n+1)
        # res[1] = 1
        bench = 2
        for i in range(1,n+1):
            if i == bench*2:
                bench = bench * 2
            print(bench,i)
            res[i] = res[i-(bench)]+1
        print(res)
        return res
            # 0 1 2 3 4 5 6 7 8 9 10

        