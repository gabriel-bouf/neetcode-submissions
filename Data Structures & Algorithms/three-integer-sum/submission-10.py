class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        S= sorted(nums)
        res = []

        for i in range(len(S)):
            val = S[i]

            l_id , r_id = i+1 , len(S)-1
            while l_id < r_id:
                #print(l_id,r_id,i,"l=",[val, S[l_id] , S[r_id]] )
                if S[l_id] + S[r_id] + val ==0 :
                    res.append( [val, S[l_id] , S[r_id]] ) if [val, S[l_id],S[r_id]] not in res else None
                    l_id +=1
                    r_id -=1

                elif S[l_id] + S[r_id] + val < 0 :
                    l_id +=1
                else: 
                    r_id -=1
        
        return res