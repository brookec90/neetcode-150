class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # calc matrix dimensions 
        rows = len(matrix)
        cols = len(matrix[0])

        # init vertical search boundaries
        top = 0 
        bottom = rows - 1

        # binary search
        while top <= bottom:
            row = (top + bottom) // 2 

            if target > matrix[row][cols - 1]:
                top = row + 1 
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        
        # no suitable row found
        if top > bottom:
            return False
        
        # init horizontal search boundaries
        left = 0 
        right = cols - 1

        # binary search through rows
        while left <= right:
            mid = (left + right) //2

            if matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] > target:
                right = mid - 1 
            else:
                return True
        
        #if target not found
        return False
        
        