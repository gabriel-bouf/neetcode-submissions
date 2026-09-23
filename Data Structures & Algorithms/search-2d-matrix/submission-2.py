class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L_l = 0

        L_r = len(matrix) - 1 
        found = False
        while L_l <= L_r: 
            mid = (L_l +L_r)//2
            if matrix[mid][0]<=target and matrix[mid][-1]>=target:
                found = True
                break

            elif matrix[mid][-1] <target:
                L_l = mid + 1 
            elif matrix[mid][-1] >target:
                L_r = mid -1

        if not found:
            return False

        l, r = 0, len(matrix[0]) -1
        while l<=r:
            m = (l+ r) //2
            if matrix[mid][m]> target:
                r = m-1
            elif matrix[mid][m]< target:
                l = m +1
            elif matrix[mid][m] == target:
                return True

        return False 