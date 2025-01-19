def gcdOfStrings(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    def isDivisible(length):
        if len1 % length or len2 % length:
            return False
        factor1 = len1 // length
        factor2 = len2 // length
        substring = str1[:length]
        return substring * factor1 == str1 and substring * factor2 == str2

    # to find largest divisor, start from back
    for l in range(min(len1, len2), 0, -1):
        if isDivisible(l):
            return str1[:l]
    return ''

# method 2
def recursion(str1, str2):
    if str1 + str2 != str2 + str1:
        return False
    if str1 == str2:
        return str1
    # str 1 bigger
    if len(str1) > len(str2):
        return recursion(str1[len(str2):], str2)
    # str 2 bigger
    return recursion(str1, str2[len(str1):])

# mathematical way
def gcdOfStrings(str1, str2):
    # INTUTION: both strings contains multiples of the identical "substring", their concatenation must be consistent both ways
    if str1 + str2 != str2 + str1:
        return ""
    
    # if exist, find the substring
    def gcd(x,y):
        if y == 0:
            return x
        else:
            return gcd(y, x%y)

    max_length = gcd(len(str1), len(str2))
    return str1[:max_length]