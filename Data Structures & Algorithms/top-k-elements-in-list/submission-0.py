class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #nums_sorted=sorted(nums)
        count = collections.defaultdict(int)
        for elem in nums:
            count[elem] +=1

        res= []
        for i in range(k):
            max_freq=0
            most_freq_int=0
            for key,value in count.items():
                if value>max_freq:
                    max_freq=value
                    most_freq_int=key
            count[most_freq_int]=-1
            res.append(most_freq_int)
        return res