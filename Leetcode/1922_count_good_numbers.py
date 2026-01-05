class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = (10**9) + 7
        # each even position has [0, 2, 4, 6, 8] - 5 choices
        # each odd position has [2, 3, 5, 7] - 4 choices
        # total choices - (5^even_positions) * (4^odd_positions)
        odd_positions = n // 2
        even_positions = (n+1) // 2
        def x_pow(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            if n%2==0:
                return x_pow((x*x)%MOD, n//2)
            else:
                return (x*x_pow((x*x)%MOD, n//2)) % MOD
        ans = (x_pow(5, even_positions) * x_pow(4, odd_positions)) % MOD
        return ans