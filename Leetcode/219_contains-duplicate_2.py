class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashset = {}
        for i in range(0, len(nums)):
            if nums[i] in hashset and abs(hashset[nums[i]] - i) <= k:
                return True
            hashset[nums[i]] = i
        return False 

### Alternate approach

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        store = defaultdict(list)
        for i in range(len(nums)):
            store[nums[i]].append(i)
        for v in store.values():
            print(v)
            if len(v) > 1:
                for i in range(len(v)-1):
                    if abs(v[i] - v[i+1]) <= k:
                        return True
        return False

# Time complexity: O(N)
# Space complexity: O(N)