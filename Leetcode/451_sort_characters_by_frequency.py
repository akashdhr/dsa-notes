from collections import Counter, defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        buckets = defaultdict(list)
        res = []

        for c, cnt in count.items():
            buckets[cnt].append(c)
        
        for i in range(len(s), 0, -1):
            for c in buckets[i]:
                res.append(c * i)
        return ''.join(res)
        