class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)

        if int(s[0])>0 :
            dp[0] = 1 
        else :
            return 0
        # un zero -> correspond a X0 avec X 1 ou 2
        for i in range(1,len(s)):

            if s[i] not in "0":
                dp[i] = dp[i] + dp[i-1]  
            
            if s[i-1:i+1] <="26" and  s[i-1:i+1] >= "10":
                if i>1:
                    dp[i] = dp[i] + dp[i-2]
                else:
                    dp[i]+=1
        return dp[-1]
