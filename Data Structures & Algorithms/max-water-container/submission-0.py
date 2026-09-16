class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l_i =0
        n=len(heights)
        r_i= n-1
        maxA= 0
        
        while l_i< r_i:
            V = (r_i - l_i ) * min(heights[l_i],heights[r_i])
            
            maxA = max(maxA , V )
            if heights[l_i] < heights[r_i]:
                l_i +=1
            else :
                r_i -=1
        return maxA
        