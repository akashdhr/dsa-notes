# Time complexity: O(N!*N)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []
        # col = column index
        def solve(col, board, n, ans):
            if col == n:
                temp = [''.join(i) for i in board]
                ans.append(temp)
                return
            for row in range(0, n):
                if safe(row, col, board, n):
                    board[row][col] = 'Q'
                    solve(col + 1, board, n, ans)
                    board[row][col] = '.'
        def safe(row, col, board, n):
            # Upper diagonal
            rowc = row
            colc = col
            while rowc>=0 and colc>=0:
                if board[rowc][colc] == 'Q':
                    return False
                rowc -= 1
                colc -= 1
            # Left row
            rowc = row
            colc = col
            while colc>=0:
                if board[rowc][colc] == 'Q':
                    return False
                colc -= 1
            # Lower diagonal
            rowc = row
            colc = col
            while rowc<n and colc>=0:
                if board[rowc][colc] == 'Q':
                    return False
                rowc += 1
                colc -= 1
            return True
        solve(0, board, n, ans)
        return ans

## Optimised approach
# Time complexity: O(N!)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []
        rows = set()
        upper_diag = set() # row - col
        lower_diag = set() # row + col
        # col = column index
        def solve(col, board, n, ans):
            if col == n:
                temp = [''.join(i) for i in board]
                ans.append(temp)
                return
            for row in range(n):
                if row in rows or (row - col) in upper_diag or (row+col) in lower_diag:
                    continue
                board[row][col] = 'Q'
                rows.add(row)
                upper_diag.add(row-col)
                lower_diag.add(row+col)
                solve(col+1, board, n, ans)
                board[row][col] = '.'
                rows.remove(row)
                upper_diag.remove(row-col)
                lower_diag.remove(row+col)
            return
        
        solve(0, board, n, ans)
        return ans