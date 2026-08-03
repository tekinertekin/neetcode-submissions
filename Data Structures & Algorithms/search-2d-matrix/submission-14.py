class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width = len(matrix[0])
        l = 0
        r = (len(matrix) * len(matrix[0])) - 1
        while l <= r:
            mid = l + (r - l) // 2
            col, row = mid%width, mid // width
            if matrix[row][col] > target:
                r = mid - 1
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                return True
        return False
        