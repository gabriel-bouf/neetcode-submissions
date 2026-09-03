import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """left_prod=1
        right_prod=math.prod(nums)
        res = []
        for i in range(len(nums)):
            right_prod = int(right_prod/nums[i])
            res_left.append(left_prod*right_prod)
            left_prod*=nums[i]

        n= len(nums)
        left_prod=[1]
        for i in range(1,n-1):
            left_prod.append(nums[i])
        return res"""
        n= len(nums)
        res = [1]*n
        p=1
        d=1
        for i in range(n):
            res[i]*= p
            p*=nums[i]

        for i in range(n-1,-1,-1):
            #print("i",i,d)
            res[i]*= d
            d*=nums[i]
        
        """left_list= [1]+nums[:-1]
        right_list= [1]+nums[::-1][:-1]
        res=[0]*n
        left_prod = [ math.prod(left_list[:i+1]) for i in range(n)]
        right_prod = [ math.prod(right_list[:i+1]) for i in range(len(right_list))]

        for i in range(n):
            left_prod[i] = left_list[:i+1]

        for i in range(n):
            res[i]= left_prod[i]*right_prod[n-i-1]"""
        
        return res

