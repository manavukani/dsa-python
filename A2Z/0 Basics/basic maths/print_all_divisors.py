def brute_force(n):
    arr = []
    for i in range(1, n+1):
        if n % i == 0:
            arr.append(i)
    return arr


print(brute_force(12))

# traverse only till sq root of n
# if i is a divisor of n, then n/i is also a divisor of n


def optimized(n):
    arr = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            arr.append(i)
            if i != n//i:
                arr.append(n//i)
    return arr

print(optimized(152))


# sumOfDivisors(3) = sum of divisors of 1 + sum of divisors of 2 + sum of divisors of 3 = 1 + (1+2) + (1+3) = 8

def sumOfDivisors(n):
    sum_divisors = [0] * (n + 1)
    
    for i in range(1, n+1):
        for div in range(i, n+1, i):
            sum_divisors[div] += i
            
    return sum(sum_divisors)

print(sumOfDivisors(3)) #8
print(sumOfDivisors(10)) #87