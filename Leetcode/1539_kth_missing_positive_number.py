# Linear Search
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arrSet = set(arr)
        res = 0
        for i in range(1, len(arr) + k + 1):
            if i not in arrSet:
                res += 1
                if res == k:
                    return i
                
# Binary Search
# Trick is to find the number of missing numbers before a particular index
# This can be done using the formula: missing_before_i = arr[i] - (i+1) as (i+1) is the true value for the ith index.
# To revisit this problem again