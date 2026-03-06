class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in store:
                return [store[diff], i]
            else:
                store[v] = i
# time complexity: O(N) where N is the number of elements in the input array. We traverse the array once and each lookup and insertion operation in the hash map takes O(1) time on average.
# space complexity: O(N) in the worst case when all elements in the array are distinct.