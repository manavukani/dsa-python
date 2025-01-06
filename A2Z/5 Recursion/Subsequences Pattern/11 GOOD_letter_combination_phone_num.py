# input - string of digits from 2-9
# output - list of all possible letter combinations that the number could represent

# eg. input - '23' => output - ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
# eg. input - '2' => output - ['a', 'b', 'c']


def phone_combinations(digits):
    if not digits:
        return []

    phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    result = []

    def backtrack(index, ds):
        # base case, if we have reached the end of the digits
        if index >= len(digits):
            result.append("".join(ds))
            return

        # loop through the letters corresponding to the current digit
        for letter in phone[digits[index]]:
            ds.append(letter)
            backtrack(index + 1, ds)
            ds.pop()

    backtrack(0, [])
    return result


# Time Complexity: O(4^n)
# Space Complexity: O(n)

# test cases
print(
    phone_combinations("23")
)  # ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
print(phone_combinations("2"))  # ['a', 'b', 'c']
