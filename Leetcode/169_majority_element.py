class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # Brute: Loop through every item and scan the entire array. TC: O(n^2)
        # Better: using hashing as shown. TC: O(n)+O(m) SC: O(m) where m is the size of the hashmap
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1
        for k, v in hashmap.items():
            if v > (len(nums)/2):
                return k
        # Optimal: Moore's Voting Algorithm
        # TC: O(n)
        # SC: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = nums[0]
        cnt = 0
        for i in nums:
            if cnt == 0:
                curr = i
            if i == curr:
                cnt += 1
            else:
                cnt -= 1
        return curr
#time complexity: O(n) where n is the number of elements in the input array. We traverse the array once.
#space complexity: O(1) since we are using only a constant amount of extra space to store the current candidate for majority element and its count.

        