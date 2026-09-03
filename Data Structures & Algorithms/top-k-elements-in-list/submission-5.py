class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #nums_sorted=sorted(nums)
        n=len(nums)
        count = collections.defaultdict(int)
        for elem in nums:
            count[elem] +=1

        res= []
        """for i in range(k):
            max_freq=0
            most_freq_int=0
            for key,value in count.items():
                if value>max_freq:
                    max_freq=value
                    most_freq_int=key
            count[most_freq_int]=-1
            res.append(most_freq_int)"""
        freq = [[] for i in range(n+1)]
        for key,value in count.items():
            #print(freq,value,key)
            freq[value].append(key)
        for elem in freq[::-1]:
            res+=elem
            if len(res)>=k:
                return res[:k]
        return res[:k]