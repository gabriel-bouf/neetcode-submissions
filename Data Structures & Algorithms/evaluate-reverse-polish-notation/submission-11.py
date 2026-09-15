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
        
