"""
Intution:

Digits at odd position: 2, 3, 5, 7 ---------> 4 choices
Digits at even position: 0, 2, 4, 6, 8 -----> 5 choices

- FOR EVEN LENGTH NUMBERS:
        - odd indices will be same as even indices
        - ways to fill odd indices = 4 ^ (n/2)
        - ways to fill even indices = 5 ^ (n/2)
        - total ways = 4 ^ (n/2) * 5 ^ (n/2)
- FOR ODD LENGTH NUMBERS:
        - one extra even index
        - ways to fill odd indices = 4 ^ (n/2)
        - ways to fill even indices = 5 ^ ((n+1)/2)
        - total ways = 4 ^ (n/2) * 5 ^ ((n+1)/2)

- need to use modular arithmetic to avoid overflow - 10^9 + 7
"""

def countGoodNumbers(n):
    MOD = 10**9 + 7

    def pow(x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1 / pow(x, -n)
        if n % 2 == 0:
            half = pow(x, n // 2)
            return half * half % MOD
        else:
            return x * pow(x, n - 1) % MOD

    if n % 2 == 0:
        return pow(4, n // 2) * pow(5, n // 2) % MOD
    else:
        return pow(4, n // 2) * pow(5, (n + 1) // 2) % MOD


# Time complexity: O(log(n))
print(countGoodNumbers(1))
print(countGoodNumbers(4))
print(countGoodNumbers(5))
print(countGoodNumbers(50))
