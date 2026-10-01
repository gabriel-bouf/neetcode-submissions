class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            current = nums[i]
            if current in seen:
                return [seen[current] , i]
            seen[diff] = i
        return False