class Solution:
    def letterCombinations(self, digits):
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
            if index >= len(digits):
                result.append("".join(ds))
                return

            # loop through each letter for a digit in input
            for letter in phone[digits[index]]:
                ds.append(letter)
                backtrack(index + 1, ds)
                ds.pop()

        backtrack(0, [])
        return result
