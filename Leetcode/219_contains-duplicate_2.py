class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashset = {}
        for i in range(0, len(nums)):
            if nums[i] in hashset and abs(hashset[nums[i]] - i) <= k:
                return True
            hashset[nums[i]] = i
        return False 
        

# Time complexity: O(N)
# Space complexity: O(N)