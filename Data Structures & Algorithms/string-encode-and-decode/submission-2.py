class Solution:
    def encode(self,strs):
        encoded_string= ""

        for word in strs:
            encoded_string += str(len(word)) + "#" + word
        return encoded_string
    
    def decode(self,strs):
        
        i=0
        decoded_string =[]
        while i < len(strs):
            if strs[i]=="#":
                length = int(strs[:i])
                j = i+1
                while j< i+1 + length:
                    j+=1
                decoded_string.append(strs[i+1:j])
                strs = strs[j:]
                i=0
            i+=1

        return decoded_string