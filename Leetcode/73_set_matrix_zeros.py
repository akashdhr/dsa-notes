class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # parser code
        rows, cols = len(matrix), len(matrix[0])
        zeroIndex = False
        for r in range(rows):
            for c in range(cols):
                # Check if the current cell is zero
                # If yes, then update the corresponding side and upper indices to zero
                # If any value in 0th column is 0 update zeroIndex to True
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    if c==0:
                        zeroIndex = True
                    else:
                        matrix[0][c] = 0
        # Update the rows first from 1,1 index
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        # Update the first row
        if matrix[0][0] == 0:
            for c in range(cols):
                matrix[0][c] = 0
        # Update the first column
        if zeroIndex == True:
            for r in range(rows):
                matrix[r][0] = 0
        return matrix    
            
