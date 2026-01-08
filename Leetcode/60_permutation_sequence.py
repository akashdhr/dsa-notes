class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def fact(x):
            if x == 0:
                return 1
            return x * fact(x-1)

        # list of available digits
        nums = []
        for i in range(1, n+1):
            nums.append(i)

        # convert k to zero-based index
        k -= 1
        ans = []

        while nums:
            # number of permutations for each possible next digit
            group_size = fact(len(nums)-1)

            # determine which bucket the k-th permutation lies in
            group_idx = k // group_size

            # update k to the index inside the selected bucket
            k %= group_size

            # select the digit and add to result
            ans.append(str(nums[group_idx]))

            # remove the used digit
            nums.pop(group_idx)

        return ''.join(ans)
    
 #  time complexity: O(N^2)
 #  space complexity: O(N)
