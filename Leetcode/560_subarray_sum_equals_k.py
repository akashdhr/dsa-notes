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
        numset = {}
        numset[0] = 1
        preSum = 0
        cnt = 0
        for i in nums:
            preSum += i
            diff = preSum - k
            if diff in numset:
                cnt += numset[diff]
            numset[preSum] = numset.get(preSum, 0) + 1
        return cnt