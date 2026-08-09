class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        row = high
        # find the lower bound
        while low <= high:
            mid = (low + high)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                row = mid 
                low = mid + 1
            else:
                high = mid - 1
        # find the value in the row
        low = 0
        high = len(matrix[0]) - 1
        while low <= high:
            mid = (low + high)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

# time complexity: O(log(M) + log(N)) where M is the number of rows and N is the number of columns in the matrix.
# space complexity: O(1) since we are using constant space to store the pointers and temporary variables.