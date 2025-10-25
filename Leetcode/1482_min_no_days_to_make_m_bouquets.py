class Solution:
    def possible(self, arr, day, m, k):
        # m = bouquets
        # k = adjacent flowers required for 1 bouquet
        cnt = 0
        bqts = 0 # stores current bouquet count
        for i in range(len(arr)):
            if arr[i] <= day:
                cnt += 1
                if cnt == k:
                    bqts += 1
                    cnt = 0
            else:
                cnt = 0
        return bqts >= m
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Base case for insufficient flowes in the array
        if m*k > len(bloomDay):
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        res = -1
        while low <= high:
            mid = (low + high)//2
            check = self.possible(bloomDay, mid, m, k)
            if check:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res