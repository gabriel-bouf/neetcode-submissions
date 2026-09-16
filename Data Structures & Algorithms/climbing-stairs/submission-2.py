class Solution:
    def __init__(self):
        self.memo ={}

    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        if n ==2:
            return 2
        elif n==0:
            return 0
        elif n==1:
            return 1
        else:
            # n-2 -> n en 2 possibilité
            res=self.climbStairs(n-2) + self.climbStairs(n-1)
            self.memo[n] = res
            return res