class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        search_row_index = -1
        low = 0
        high = rows-1

        while low <= high:
            mid = (low + high)//2
            if matrix[mid][0] <= target <= matrix[mid][cols-1]:
                search_row_index = mid
                break
            elif matrix[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1
        if search_row_index == -1:
            return False
        low = 0
        high = cols-1
        while low <= high:
            mid = (low + high)//2
            if matrix[search_row_index][mid] == target:
                return True
            elif matrix[search_row_index][mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False


# time complexity: O(log(M) + log(N)) where M is the number of rows and N is the number of columns in the matrix.
# space complexity: O(1) since we are using constant space to store the pointers and temporary variables.