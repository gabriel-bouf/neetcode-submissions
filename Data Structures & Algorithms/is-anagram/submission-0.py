class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = collections.defaultdict(int)
        t_dict = collections.defaultdict(int)
        """for (letter_s, letter_t) in s,t:
            s_dict[letter_s]+=1
            t_dict[letter_t]+=1
        return s_dict == t_dict"""
        for letter in s:
            
            s_dict[letter]+=1
        for letter in t:
            t_dict[letter]+=1
        return s_dict == t_dict