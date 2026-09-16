class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=2:
            return max(nums)
        dp1=[0]* (n-1)
        dp2=[0]* (n-1)
        n1= nums[:-1] 
        n2 = nums[1:]
        dp1[0] = n1[0]
        dp2[0] = n2[0]
        dp1[1] = max(n1[:2])
        dp2[1] = max(n2[:2])

        for i in range(2,n-1):
            dp1[i] = max(n1[i] + dp1[i-2] , dp1[i-1])
            dp2[i] = max(n2[i] + dp2[i-2] , dp2[i-1])
        return max(dp1[n-2], dp2[n-2])