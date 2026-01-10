class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hset = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            hset[i] = hset.get(i, 0) + 1
        for i, count in hset.items():
            freq[count].append(i)
        # read freq array from behind
        for i in range(len(freq)-1, -1, -1):
            for j in freq[i]:
                res.append(j)
            if len(res) == k:
                return res
        return res
        
# time complexity: O(N)
# space complexity: O(N)