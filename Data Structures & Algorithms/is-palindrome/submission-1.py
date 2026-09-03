class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        valid = [chr(i) for i in range(65,91) ] + [chr(i) for i in range(97,123) ] + [str(i) for i in range(10)]
        valid = set(valid)
        #print(valid)
        #print(chr(65),ord("a"))
        """for i in range (n):
            print(s[i],s[i].lower(), s[n-i-1].lower())
            j = i
            while s[i].lower() != s[n-j-1].lower():
                j+=1
            if i>n-j-1:
                return False
        return True"""
        g, d = 0, n-1
        
        while g<d:
            if s[g] not in valid:
                g+=1
            elif s[d] not in valid:
                d-=1
            elif s[g].lower() !=s[d].lower():
                print(s[g].lower(),s[d].lower() )
                return False
            else:
                g+=1
                d-=1
        return True
