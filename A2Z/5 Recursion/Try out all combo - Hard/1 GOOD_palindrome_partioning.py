# input - string s
# output - all possible palindrome partitioning (subsets) of s

# eg. input - "aab"
# output - [["a","a","b"],["aa","b"]]

"""

- check if partition is possible --> left is palindrome, else skip
- do the same for the right side
- if both are palindrome, append to the result

                    aabb
        a|abb                        aa|bb                      0..2 not palindrome     0..3 not palindrome
    a|a|bb                    aa|b|b        a|a|bb|                   skip                    skip
a|a|b|b   a|a|bb|            aa|b|b|        
a|a|b|b|   

- stop when the partition is equal to the length of the string (reach end)
"""


def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def backtrack(index, s, path, ans):
    if index == len(s):
        ans.append(path[:])
        return

    for i in range(index, len(s)):
        # left is palindrome, check right recursively
        if is_palindrome(s, index, i):
            path.append(s[index : i + 1])
            backtrack(i + 1, s, path, ans)
            path.pop()


# Time Complexity: O(n * 2^n)
# Space Complexity: O(n)
def partition(s):
    ans = []
    path = []  # ds
    backtrack(0, s, path, ans)
    return ans


# test cases
print(partition("aab"))  # [["a","a","b"],["aa","b"]]
print(partition("aabb")) # [["a","a","b","b"],["a","a","bb"],["aa","b","b"],["aa","bb"]]