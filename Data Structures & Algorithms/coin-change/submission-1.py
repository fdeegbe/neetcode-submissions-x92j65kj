class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        q = deque([0])
        seen = [False] * (amount + 1)
        seen[0] = True
        res = 0

        while q:
            res +=1 # next level of bfs
            print(q)
            for _ in range(len(q)):
                curr = q.popleft()

                for coin in coins:
                    if curr + coin < len(seen) and seen[coin+curr] != True:
                        seen[coin+curr] = True
                        q.append(coin+curr)
                    if curr+coin == amount:
                        return res
        return -1
            