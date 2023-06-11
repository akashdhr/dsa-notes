class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute: Check all possible pairs . TC: O(n^2)
        # Better: using hashing as shown. TC: O(n) SC: O(n)
        prevMap = {}  # val -> index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
    
        