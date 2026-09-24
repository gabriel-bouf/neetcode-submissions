from math import inf 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return None
        min_dp = [ inf for _ in range(len(nums))]
        max_dp = [ -inf for _ in range(len(nums))]
        #sol opti pour liste de taille i +1
        min_dp[0] = nums[0]
        max_dp[0] = nums[0]
        for i in range(1,len(max_dp)):
            #dp[1] = max nums
            # dp 2 = max (produit dans nums, dp[1] )
            min_dp[i] = min([min_dp[i-1] * nums[i] , nums[i] , max_dp[i-1]*nums[i]])
            max_dp[i] = max([min_dp[i-1] * nums[i] , nums[i] , max_dp[i-1]*nums[i]])
        #print(min_dp,max_dp)
        #return max(min_dp[-1],max_dp[-1])
        res = max_dp[0]
        for i in range(len(max_dp)):
            res = max([res,max_dp[i],min_dp[i]])
        return res