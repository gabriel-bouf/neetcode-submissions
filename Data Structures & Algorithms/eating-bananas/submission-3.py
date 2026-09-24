class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        if h < len(piles): 
            return None
        k_min=1
        k_max = max(piles)


        while k_min<=k_max :
            
            count = 0
            k_mid = (k_min + k_max) //2

            for i in range(len(piles)):
                if piles[i]%k_mid!=0 :
                    count += piles[i]//k_mid + 1 
                else :
                    count+= piles[i]//k_mid
                #print(count, piles[i], k_min,k_mid,k_max)
                
            if count <=h:
                k_max = k_mid - 1 
            elif count>h:
                k_min = k_mid +1
            
        return k_min