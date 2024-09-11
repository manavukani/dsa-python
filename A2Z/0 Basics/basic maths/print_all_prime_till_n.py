# Sieve of Eratosthenes

'''

n = 100

list from 2 to n
mark all as prime
start from 2
mark all its multiple >= square of 2 as not prime
move to next unmarked number
repeat the process till sqrt(n)

'''


def SieveOfEratosthenes(n):

    prime = [True for i in range(n+1)]  # mark all as prime
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    # print all prime numbers
    for p in range(2, n+1):
        if prime[p]:
            print(p)

n = 153121
print("Prime numbers smaller than or equal to", n, "are:")
SieveOfEratosthenes(n)
