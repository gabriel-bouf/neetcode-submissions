class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #registered = collections.defaultdict(list)
        registered = {}
        """for i in range(len(strs)):
            word ="".join(sorted(strs[i]))
            #if word in registered:
                #on ajoute a la value (list) le mot
            registered.word.append(strs[i])"""
        for i in range(len(strs)):
            word ="".join(sorted(strs[i]))
            #print(word,registered.keys())
            if word not in registered:
                registered[word] = [strs[i]]
            else:
                registered[word].append(strs[i])
        #comment dict.values
        
        return list(registered.values())