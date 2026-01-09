class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ds = []
        res = set()
        used = [False] * len(digits)
        def find(ds):
            if len(ds) == 3:
                if ds[0] != 0 and ds[-1]%2 == 0:
                    res.add(''.join(map(str, ds.copy())))
                return
            for i in range(len(digits)):
                if used[i]:
                    continue
                used[i] = True
                ds.append(digits[i])
                find(ds)
                ds.pop()
                used[i] = False
        find(ds)
        return len(res)