class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        rows = len(matrix)
        low = 0
        high = rows - 1
        to_search = -1
        # find the row where the value might be present
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target <= matrix[mid][cols-1]:
                to_search = mid
                break
            elif matrix[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1
        if to_search == -1:
            return False
        # now apply bs on to_search row
        low = 0
        high = cols - 1
        while low <= high:
            mid = (low + high)//2
            if matrix[to_search][mid] == target:
                return True
            elif matrix[to_search][mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
# time complexity: O(log M + log N) where M is the number of rows and N is the number of columns. why? because we are applying binary search twice.
# space complexity: O(1) as we are using only constant extra space.