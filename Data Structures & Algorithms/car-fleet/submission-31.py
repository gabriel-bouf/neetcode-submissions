class Solution:
    def myfunc(self,tup):
        # si x int: x-10, len(str), TOUT est possible
        return tup[0]


    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # on fait une stack ou le dernier elt est toujours le plus lent que les autres, et si on new arrivant est plus rapide, on clean toute la stack et on recommence.
        res=1
        L = [(pos, spe ) for pos, spe in zip(position,speed)]
        Val =sorted(L,reverse=True, key=self.myfunc)

        stack =[]
        for i in range(len(Val)):
            pos= Val[i][0]
            spe = Val[i][1]
            if not stack:
                stack.append( (pos,spe))

            elif (target - pos) / spe > (target - stack[-1][0]) / stack[-1][1]:
                stack= [(pos, spe)]
                res+=1
            else:
                continue
            print(stack, (target - pos) / spe , (target - stack[-1][0]) / stack[-1][1])
        return res 

