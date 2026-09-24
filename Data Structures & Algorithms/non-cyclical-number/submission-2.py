class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        number = n
        while number not in seen:
            seen.add(number)
            cyc = 0
            for s in str(number):
                digit = int(s)
                cyc += digit**2
                print(number,digit,cyc)
            if cyc ==1:
                return True
            number = cyc

        return False