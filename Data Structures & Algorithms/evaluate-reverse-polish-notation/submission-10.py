class Solution:
    def apply_operator(self, val1: int, val2: int, ope: str) -> int:
        if ope =='+':
            return val1 + val2
        elif ope== '-':
            return val1 - val2
        elif ope== '*':
            return val1 * val2
        elif ope== '/':
            return int(val1 / val2)
        return None

    def evalRPN(self, tokens: List[str]) -> int:
        operators = set({'+', '-', '*','/'})
        stack = []
        for (i,string) in enumerate(tokens):
            if string in operators:
                v1= stack[-2]
                v2= stack[-1]
                stack.pop()
                stack.pop()
                res= self.apply_operator(v1,v2,string)
                stack.append(res)
            elif string not in operators:
                stack.append(int(string))
        return stack[-1]
        """       
        if not tokens:
            return 0
        elif len(tokens)==1:
            return int(tokens[0])
        else:
            initial_val1=int(tokens[0])
            initial_val2=int(tokens[1])
            initial_ope=tokens[2]
            res = self.apply_operator(initial_val1,initial_val2,initial_ope)
            i=3
            print(tokens)
            while i < len(tokens):
                string= tokens[i]
                if string in operators:
                    if tokens[i-1] not in operators:

                        res = self.apply_operator(res,int(tokens[i-1]),string)
                    
                i+=1"""
        return res
