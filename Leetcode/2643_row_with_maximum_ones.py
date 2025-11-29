class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxCount = -1
        maxRow = 0
        for i,r in enumerate(mat):
            rowSum = sum(r)
            if rowSum > maxCount:
                maxCount = rowSum
                maxRow = i
        return [maxRow, maxCount]