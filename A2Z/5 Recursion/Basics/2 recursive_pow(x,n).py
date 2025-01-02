# TC: O(logn)
def myPow_recursive(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / myPow(x, -n)
    if n % 2 == 0:
        half = myPow(x, n // 2)
        return half * half
    else:
        return x * myPow(x, n - 1)


def myPow(x, n):
    if n < 0:
        x = 1 / x
        n = -n

    result = 1
    current_product = x
    while n > 0:
        if n % 2 == 1:
            result *= current_product
        current_product *= current_product
        n //= 2

    return result
