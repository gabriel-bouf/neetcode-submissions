class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = []

        for (i,t) in enumerate(temperatures):
            if not stack:
                stack.append((i,t))

            elif stack and stack[-1][1]>= t:
                stack.append((i,t))
            elif stack:
                #non vide mais pas decroissant
                j = -1
                while stack and stack[j][1]< t:
                    res[stack[j][0]] =  i - stack[j][0]
                    stack.pop()

                stack.append((i,t))
            #print("end i",stack,"res",res)
        return res