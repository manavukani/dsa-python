# brute force
def find_gcd(n, m):
    gcd = 1
    for i in range(1, min(n, m)+1):
        if n % i == 0 and m % i == 0:
            gcd = i

    return gcd


print(find_gcd(9, 12))

# better approach - iterate from the minimum of N1 and N2 down to 1
# we reduce the number of iterations because we start from the potentially largest common factor and work downwards.
# time complexity remains O(min(N1, N2)) but in practice, it will execute fewer iterations on average.


def find_gcd2(n, m):
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            return i

    return 1  # if not found


print(find_gcd2(20, 15))

# ----------- Euclidean algorithm ------------
# To find the GCD of n1 and n2 where n1 > n2:
# Repeatedly subtract the smaller number from the larger number until one of them becomes 0.
# Once one of them becomes 0, the other number is the GCD of the original numbers.


def eculedian_gcd(n, m):
    while n != 0 and m != 0:
        if n > m:
            n -= m
        else:
            m -= n
            
    return n if n != 0 else m

print(eculedian_gcd(33, 9))