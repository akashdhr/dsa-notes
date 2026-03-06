class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)
        return False

# time complexity: O(N) where N is the number of elements in the input array. We traverse the array once and each lookup and insertion operation in the hash set takes O(1) time on average.
# space complexity: O(N) in the worst case when all elements in the array are distinct, we will have to store all elements in the hash set.