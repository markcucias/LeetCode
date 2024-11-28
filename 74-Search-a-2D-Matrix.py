class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])
        lo_m, hi_m = 0, m - 1

        if target >= matrix[m-1][0]:
            mid_m = m - 1
        else:
            mid_m = lo_m + (hi_m - lo_m) // 2
            while lo_m < hi_m:
                if matrix[mid_m][0] <= target < matrix[mid_m + 1][0]:
                    break
                if matrix[mid_m][0] > target:
                    hi_m = mid_m
                else:
                    lo_m = mid_m + 1
                mid_m = lo_m + (hi_m - lo_m) // 2


        list = matrix[mid_m]
        m = len(list)
        lo = 0
        hi = m - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if list[mid] == target:
                return True
            if list[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return False
        
        
    