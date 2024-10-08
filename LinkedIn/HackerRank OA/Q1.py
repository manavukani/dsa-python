# Break a palindrome

# change exactly one char so string is:
# => alphabetically lower than original
# => new is lowest value that can be created by making onyl 1 change
# => not a palindrome

# i/p: 'aaabbaaa' can be modified as 'aaaabaaa' or 'aaabaaaa'
# o/p: 'aaaabaaa'

def break_palindrome(word):
    n = len(word)

    if n == 1:
        return "IMPOSSIBLE"

    if word.count('a') == n or (word[:-1].count('a') == n-1 and word[-1] == 'b'):
        return "IMPOSSIBLE"

    for i in range(n//2):
        if word[i] != 'a':
            return word[:i] + 'a' + word[i+1:]

    return word[:-1] + 'b'

a = ['bab', 'aaa', 'acca']

for ele in a:
    print(break_palindrome(ele))
    print()
