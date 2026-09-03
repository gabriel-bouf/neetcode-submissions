class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_sorted = sorted(nums)
        for idx in range(len(nums_sorted)-1):
            if nums_sorted[idx] == nums_sorted[idx+1]:
                return True
        return False