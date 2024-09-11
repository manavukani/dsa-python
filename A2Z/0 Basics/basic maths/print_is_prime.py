def is_prime(n):
    for i in range(1, n+1):
        if n % i == 0:
            if i != 1 and i != n:
                return False
    return True


print(is_prime(7))  # True


# If a number n is not prime: n = a * b
# a and b can't be both greater than the square root of n, since then the product a * b would be greater than sqrt(n) * sqrt(n) = n. 
# So in any factorization of n, at least one of the factors must be less than or equal to the square root of n
# if we can't find, n must be a prime.



def is_prime_optimized(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print(is_prime_optimized(9))  # False