# myAtoi(string s) function, which converts a string to a 32-bit signed integer.

'''
1. Ignore white spaces
2. Return 0 if the first character is not a number or a sign
3. Determine the sign by checking if the next character is + or -
4. For out of the 32-bit signed integer range [-2^31, 2^31 - 1], remain in the range

'''
# TC = O(n)
def myAtoi(s):
    s = s.strip()
    if not s:
        return 0
    isNegative = False
    start = 0

    if s[0] == "-":
        isNegative = True
        start = 1
    elif s[0] == "+":
        start = 1
    elif s[0].isnumeric():
        start = 0

    number = 0
    while start < len(s) and s[start].isnumeric():
        number = number * 10 + int(s[start])
        start += 1
    if isNegative:
        number = -number

    # cannot exceed max and min
    number = max(min(number, 2**31 - 1), -(2**31))
    return number


def myAtoi_recursive(s):
    s = s.strip()
    if not s:
        return 0
    isNegative = False
    start = 0

    if s[0] == "-":
        isNegative = True
        start = 1
    elif s[0] == "+":
        start = 1
    elif s[0].isnumeric():
        start = 0

    def helper(s, index, number, isNegative):
        if index >= len(s) or not s[index].isnumeric():
            return -number if isNegative else number

        number = number * 10 + int(s[index])
        return helper(s, index + 1, number, isNegative)

    result = helper(s, start, 0, isNegative)
    number = max(min(result, 2**31 - 1), -(2**31))
    return number
