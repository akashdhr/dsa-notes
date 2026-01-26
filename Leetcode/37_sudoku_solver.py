class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(row, col, num, board):
            # Check row
            for c in range(9):
                if board[row][c] == num:
                    return False
            # Check col
            for r in range(9):
                if board[r][col] == num:
                    return False
            base_row = (row // 3) * 3
            base_col = (col // 3) * 3
            # Check box
            for r in range(base_row, base_row + 3):
                for c in range(base_col, base_col + 3):
                    if board[r][c] == num:
                        return False
            return True

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '.':
                    for num in map(str, range(1, 10)):
                        if isValid(row, col, num, board):
                            board[row][col] = num
                            if self.solveSudoku(board):
                                return True
                            else:
                                board[row][col] = '.'
                    return False
        return True            
    
    #time complexity: O(9^(n*n)) where n is 9 here. In the worst case, we might have to fill all cells and for each cell we have 9 options.
    #space complexity: O(1) as we are modifying the board in place and not