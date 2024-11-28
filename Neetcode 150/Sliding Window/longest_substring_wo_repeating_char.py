# When first duplicate occurs, slide the window to the right 
# until the duplicate is removed from the window.
def lengthOfLongestSubstring(self, s: str) -> int:
    curWindow = set()
    L = 0
    maxi = 0

    for R in range(len(s)):
        while s[R] in curWindow:
            # remove left ele from window
            curWindow.remove(s[L])
            L += 1

            # if not in window, add
        curWindow.add(s[R])

        maxi = max(maxi, R - L + 1)  # if new window size bigger, update

    return maxi # length of substring