# Implement pow(x, n) % d.
# Note that remainders on division cannot be negative. In other words, make sure the answer you return is non-negative integer.

def pow_mod(x, n, d):
    if d == 1:
        return 0  # any number mod 1 is 0
    
    result = 1
    base = x % d  # Take x mod d initially to avoid overflow
    
    while n > 0:
        if n % 2 == 1:  # If n is odd, multiply the result with base
            result = (result * base) % d
        
        base = (base * base) % d  # Square the base
        n = n // 2  # Reduce n by half
        
    # Ensure the result is non-negative
    return result if result >= 0 else (result + d)

x = 6
n = 7
d = 4
print(pow_mod(x, n, d))  # 1