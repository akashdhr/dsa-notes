class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for row in range(len(matrix)):
            self.prefix[row][0] = matrix[row][0]
            for col in range(1, len(matrix[0])):
                self.prefix[row][col] = matrix[row][col] + self.prefix[row][col-1]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for row in range(row1, row2+1):
            if col1 > 0:
                res += self.prefix[row][col2] - self.prefix[row][col1-1]
            else:
                res += self.prefix[row][col2]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# time complexity: O(M) where M is the number of rows in the specified region (row2 - row1 + 1) since we need to iterate through each row in the specified region to calculate the sum.
# space complexity: O(N) where N is the number of columns in the input matrix since we are using a prefix sum array to store the cumulative sums for each row, which requires additional space proportional to the number of columns in the matrix.