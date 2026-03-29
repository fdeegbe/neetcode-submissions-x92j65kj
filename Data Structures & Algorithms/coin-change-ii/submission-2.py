class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [[0] * (amount + 1) for _ in range(len(coins))]
        for i in range(len(coins)):
            memo[i][0] = 1

        # print(memo)

        for i in range(len(coins)):
            coinVal = coins[i]
            for j in range(1,amount+1):
                if j - coinVal >= 0:
                    memo[i][j] += memo[i][j - coinVal]
                if i > 0:
                    memo[i][j] += memo[i-1][j]
            # print(memo)
        return memo[-1][-1]
        

