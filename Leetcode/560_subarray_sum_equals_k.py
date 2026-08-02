'''
First, we will declare a map to store the prefix sums and their counts.
Then, we will set the value of 0 as 1 on the map.
Then we will run a loop(say i) from index 0 to n-1(n = size of the array).
For each index i, we will do the following:
We will add the current element i.e. arr[i] to the prefix sum.
We will calculate the prefix sum i.e. x-k, for which we need the occurrence.
We will add the occurrence of the prefix sum x-k i.e. mpp[x-k] to our answer.
Then we will store the current prefix sum in the map increasing its occurrence by 1.
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = 0
        store = dict()
        store[0] = 1
        ans = 0
        for i in range(len(nums)):
            preSum += nums[i]
            diff = preSum - k
            if diff in store:
                ans += store[diff]
            store[preSum] = store.get(preSum, 0) + 1
        return ans

# time complexity: O(N) where N is the number of elements in the input array. We traverse the array once and each lookup and insertion operation in the hash map takes O(1) time on average.
# space complexity: O(N) in the worst case when all prefix sums are distinct, we will have to store all prefix sums in the hash map.