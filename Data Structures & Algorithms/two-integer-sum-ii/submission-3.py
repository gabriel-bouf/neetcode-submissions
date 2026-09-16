class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right_idx = len(numbers) - 1
        left_idx=0

        while numbers[right_idx] + numbers[left_idx] != target:
            #print(left_idx, right_idx)
            if numbers[right_idx] + numbers[left_idx] < target :
                left_idx += 1
            elif numbers[right_idx] + numbers[left_idx] > target :
                right_idx -= 1
            else:
                #on a tester tt les combi avec numbers[right_idx] et on a depasser et != target
                right_idx -= 1
                left_idx = 0


        return [left_idx+1, right_idx+1]