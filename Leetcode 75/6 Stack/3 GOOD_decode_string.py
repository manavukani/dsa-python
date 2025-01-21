class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_string = ''
        curr_number = 0
        
        for c in s:
            if c.isdigit():
                curr_number = curr_number * 10 + int(c)
            elif c == '[':
                stack.append((curr_string, curr_number))
                curr_string = ''
                curr_number = 0
            elif c == ']':
                prev_string, num = stack.pop()
                curr_string = prev_string + num * curr_string
            else:
                curr_string += c
                
        return curr_string