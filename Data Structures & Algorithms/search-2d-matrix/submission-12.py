class Solution:
    def _helper(self, pos: int, width: int) -> [int, int]:
        return [pos%width, pos // width]

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width = len(matrix[0])
        l = 0
        r = (len(matrix) * width) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            col, row = self._helper(mid, width)
            print(col, row , mid)
            if matrix[row][col] > target:
                r = mid - 1
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                return True
        return False
        