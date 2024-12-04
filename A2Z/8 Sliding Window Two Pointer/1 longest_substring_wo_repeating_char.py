def lengthOfLongestSubstring(s):
    curWindow = set()
    L = 0
    maxi = 0

    for R in range(len(s)):
        while s[R] in curWindow:
            curWindow.remove(s[L])  # left most ele of window
            L += 1

        curWindow.add(s[R])  # if not set, add to window

        maxi = max(maxi, R - L + 1)  # if new window size bigger, update

    return maxi
