from math import inf
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [ inf for _ in range(amount +1)]
        dp[0] = 0

        for i in range(len(dp)):
            for c in coins:
                if i+c< len(dp):
                    dp[i+c] = min (dp[i+c],  1 + dp[i])

        if dp[-1] == inf:
            return -1
        return dp[-1]