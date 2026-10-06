class Solution:
    def encode(self,strs):
        encoded_string= ""

        for word in strs:
            encoded_string += str(len(word)) + "#" + word
        return encoded_string
    
    def decode(self,strs):
        
        i=0
        j=0
        decoded_string =[]
        while i < len(strs):
            if strs[i]=="#":
                length = int(strs[j:i])
                decoded_string.append(strs[i+1:i+1+length])
                #strs = strs[i+1+length:]
                j = i+1+length
                i= i+1+length

            i+=1

        return decoded_string