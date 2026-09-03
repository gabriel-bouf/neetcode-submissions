class Solution:
    def isValid(self, s: str) -> bool:
        dic ={')': '(', '}': '{',']': '['}
        L=[]
        if len(s)<2:
            return bool(1-len(s))
        for char in s:
            if char not in dic:
                L.append(char)

            
            elif len(L )>0 and dic[char] != L[-1]:
                return False
            else:
                if len(L )>0:
                    L.pop(-1)
                else:
                    return False
        if len(L)>0:
            return False
        return True
