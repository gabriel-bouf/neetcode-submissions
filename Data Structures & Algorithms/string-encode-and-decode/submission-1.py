class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string))
            res += "-"
            res += string
            
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        while len(s)>0:
            nb= s.split("-")[0]
            #print(nb)
            digits=len(nb)
            nb = int(nb)
            #print("nb",nb,type(nb))
            word = s[digits+1:digits+1+nb]
            #print(word)
            res.append(word)
            s = s[digits+1+nb:]
        return res
        