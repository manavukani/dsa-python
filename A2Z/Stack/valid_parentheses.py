class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_map = {
            ')':'(',
            ']':'[',
            '}':'{',
        }
        for char in s:
            if char in valid_map.values():
                stack.append(char)
            if char in valid_map.keys():
                if not stack or stack[-1] != valid_map[char]:
                    return False
                else:
                    stack.pop()
        return stack == []