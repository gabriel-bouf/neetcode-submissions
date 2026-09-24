class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word = set(wordDict)
        dp = [False for _ in range(len(s)+1)]
        dp[0]= True #if s[0] in wordDict else False
        for i in range(1,len(s)+1):
            
            for j in range(i):
                
                if s[j:i] in word and dp[j] == True:
                    dp[i]=True
                    break
            print(dp)
        return dp[-1]
