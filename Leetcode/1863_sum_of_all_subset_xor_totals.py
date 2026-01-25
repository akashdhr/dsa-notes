class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.ans = 0
        def find(ind, temp):
            if ind == len(nums):
                xor_ans = 0
                for i in temp:
                    xor_ans ^= i
                self.ans += xor_ans
                return
            temp.append(nums[ind])
            find(ind + 1, temp)
            temp.pop()
            find(ind + 1, temp)
        find(0, [])
        return self.ans

# time complexity: O(N * 2^N) where N is the number of elements in the input array. There are 2^N subsets, and for each subset, we may need to compute the XOR which takes O(N) time in the worst case.
# space complexity: O(N) for the recursion stack and the temporary list used to store the current subset.

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.ans = 0
        def find(ind, temp):
            if ind == len(nums):
                self.ans += temp
                return
            find(ind + 1, temp ^ nums[ind])
            find(ind + 1, temp)
        find(0, 0)
        return self.ans

# time complexity: O(2^N) where N is the number of elements in the input array. There are 2^N subsets, and we compute the XOR in constant time for each subset.
# space complexity: O(N) for the recursion stack.