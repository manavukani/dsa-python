# print 1 to N recursively

def print1toN(N):
    if N == 0:
        return
    print1toN(N-1)
    print(N)


print1toN(5)

print("--------------------")


def printNto1(N):
    if N == 0:
        return
    print(N)
    printNto1(N-1)


printNto1(5)

print("--------------------")


def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)

print(sum(5))

print("--------------------")

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))