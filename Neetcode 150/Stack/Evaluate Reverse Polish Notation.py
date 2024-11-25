class Solution:
    def evalRPN(self, tokens):
        stack = []
        for char in tokens:
            if char == '+':
                stack.append(stack.pop() + stack.pop())
            elif char == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b-a) # order matters
            elif char == '*':
                stack.append(stack.pop() * stack.pop())
            elif char == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a)) # order matters
            else:
                stack.append(int(char))

        return stack[0]
