import bisect
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
       
        while len(stones) > 1:
            s1,s2 = stones.pop(), stones.pop()
            print(s1,s2)
            s3 = s1-s2
            if s3:
                bisect.insort(stones, s3)
        return stones[0] if stones else 0