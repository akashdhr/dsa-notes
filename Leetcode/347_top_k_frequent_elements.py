class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        for i in nums:
            store[i] = store.get(i, 0) + 1
        freq = []
        for i,v in store.items():
            freq.append([v,i])
        freq.sort()
        ans = []
        print(freq)
        while k > 0:
            ans.append(freq.pop()[1])
            k -= 1
        return ans

        
        
# time complexity: O(N log N) where N is the number of unique elements in the input array. We count the frequency of each element in O(N) time, then we sort the frequency list which takes O(N log N) time, and finally we retrieve the top k elements which takes O(k) time.
# space complexity: O(N) where N is the number of unique elements in the input array since we are using a hash map to store the frequency of each element and a list to store the frequency and corresponding elements.