def gcdOfStrings(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    def isDivisible(length):
        if len1 % length or len2 % length:
            return False
        factor1 = len1 // length
        factor2 = len2 // length
        return str1[:length] * factor1 == str1 and str1[:length] * factor2 == str2

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
    if len(str1) > len(str2):
        return recursion(str1[len(str2):], str2)
    return recursion(str1, str2[len(str1):])
