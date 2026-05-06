class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        freq = []
        for i,j in count.items():
            temp = [j, i]
            freq.append(temp)
        freq.sort()
        res = []
        while k > 0:
            res.append(freq.pop()[1])
            k -= 1
        return res
        
# time complexity: O(N log N) where N is the number of unique elements in the input array. We count the frequency of each element in O(N) time, then we sort the frequency list which takes O(N log N) time, and finally we retrieve the top k elements which takes O(k) time.
# space complexity: O(N) where N is the number of unique elements in the input array since we are using a hash map to store the frequency of each element and a list to store the frequency and corresponding elements.