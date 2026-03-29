class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            #get the first bit
            if n & (1<<i):
                # print(i, 'YES')
                res ^= (1 << (32-i-1))
        # print(1<<33)
        return res