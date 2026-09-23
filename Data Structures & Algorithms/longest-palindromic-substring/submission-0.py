class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        #print(s[::-1])
        """dp=[["" for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i,n):
                #diag: s[i]...s[j] = s[i] et lettre = palindrome
                if j==i:
                    dp[i][j]= s[i]
                elif j==i+1 and s[i] == s[j]:
                    dp[i][j]=s[i:j+1]
                elif s[i] == s[j]:
                    dp[i][j]= s[i] + dp[i+1][j-1] + s[i]
                else: 

                

        return ""
        """

        res = ""
        reslen = 0

        for i in range(n):
            #odd 
            l, r = i ,i 
            while l>=0 and r <n and s[l]== s[r]:
                if r-l +1 > reslen:
                    res = s[l:r+1]
                    reslen = r - l + 1
                l-=1
                r+=1
            
            #even
            l, r = i ,i +1
            while l>=0 and r <n and s[l]== s[r]:
                if r-l +1 > reslen:
                    res = s[l:r+1]
                    reslen = r - l + 1
                l-=1
                r+=1
        return res
