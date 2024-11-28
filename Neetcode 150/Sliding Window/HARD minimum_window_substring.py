def minWindow(s, t):
    if t == "":
        return ""

        # char -> # occ
    countT, window = {}, {}

    # substring freq count -> countT = Counter(t)
    for char in t:
        countT[char] = 1 + countT.get(char, 0)

    L = 0

    have, need = 0, len(countT)

    res = [-1, -1]
    resLen = float('inf')

    for R in range(len(s)):
        char = s[R]
        window[char] = 1 + window.get(char, 0)

        if char in countT and window[char] == countT[char]:
            have += 1

        while have == need:
            # found smaller substring
            if (R-L+1) < resLen:
                res = [L, R]
                resLen = R-L+1

            window[s[L]] -= 1

            if s[L] in countT and (window[s[L]] < countT[s[L]]):
                have -= 1

            L += 1

    L, R = res

    if resLen != float('inf'):
        return s[L:R+1]
    else:
        return ""
