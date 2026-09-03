class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s= set(nums)
        #erase duplicates
        best=0
        for x in s:
            if x-1 not in s:
                longueur = 1
                while x+longueur in s:
                    longueur+=1
                best = longueur if longueur>best else best
        return best