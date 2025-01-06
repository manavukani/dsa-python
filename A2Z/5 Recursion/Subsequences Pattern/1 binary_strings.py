# input = size K
# output = all strings of size K without consecutive 1's

# IDEA: if ends with 0, we can add 0 or 1, BUT if ends with 1, we can only add 0


def generateAllStrings(K):

    if K <= 0:
        return

    # store the chars
    str = [0] * K

    def helper(K, str, n):
        if n == K:
            print("".join(str))
            return

        # last char is 1
        if str[n - 1] == "1":
            str[n] = "0"
            helper(K, str, n + 1)

        # last char is 0
        if str[n - 1] == "0":
            str[n] = "0"
            helper(K, str, n + 1)
            str[n] = "1"
            helper(K, str, n + 1)

    # all string start with '0'
    str[0] = "0"
    helper(K, str, 1)

    # all string start with '1'
    str[0] = "1"
    helper(K, str, 1)


K = 3
generateAllStrings(K)
