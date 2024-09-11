def check_palindrome(str):
    if len(str) <= 1:
        return True
    else:
        if str[0] == str[-1]:
            return check_palindrome(str[1:-1])
        else:
            return False

print(check_palindrome("madam"))