""" ====================== INFIX TO PREFIX AND POSTFIX ====================== """


def infix_to_prefix(expression):
    def reverse_expression(expr):
        reversed_expr = []
        for char in expr[::-1]:
            if char == "(":
                reversed_expr.append(")")
            elif char == ")":
                reversed_expr.append("(")
            else:
                reversed_expr.append(char)
        return "".join(reversed_expr)

    reversed_infix = reverse_expression(expression)
    postfix = infix_to_postfix(reversed_infix)
    return postfix[::-1]


def infix_to_postfix(expression):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    stack = []
    result = []

    for char in expression:
        if char.isalnum():  # Operand
            result.append(char)
        elif char == "(":  # Left parenthesis
            stack.append(char)
        elif char == ")":  # Right parenthesis
            while stack and stack[-1] != "(":
                result.append(stack.pop())
            stack.pop()  # Remove '('
        else:  # Operator
            while (
                stack
                and stack[-1] != "("
                and precedence.get(stack[-1], 0) >= precedence[char]
            ):
                result.append(stack.pop())
            stack.append(char)

    while stack:
        result.append(stack.pop())

    return "".join(result)


""" ====================== PREFIX TO INFIX AND POSTFIX ====================== """


def prefix_to_infix(expression):
    stack = []

    for char in reversed(expression):
        if char.isalnum():  # Operand
            stack.append(char)
        else:  # Operator
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(f"({operand1}{char}{operand2})")

    return stack[0]


def prefix_to_postfix(expression):
    stack = []

    for char in reversed(expression):
        if char.isalnum():  # Operand
            stack.append(char)
        else:  # Operator
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(f"{operand1}{operand2}{char}")

    return stack[0]


""" ====================== POSTFIX TO INFIX AND PREFIX  ====================== """


def postfix_to_prefix(expression):
    stack = []

    for char in expression:
        if char.isalnum():  # Operand
            stack.append(char)
        else:  # Operator
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(f"{char}{operand1}{operand2}")

    return stack[0]


def postfix_to_infix(expression):
    stack = []

    for char in expression:
        if char.isalnum():  # Operand
            stack.append(char)
        else:  # Operator
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(f"({operand1}{char}{operand2})")

    return stack[0]


# Test expressions
infix_expr = "(A+B)*(C-D)"
prefix_expr = "*+AB-CD"
postfix_expr = "AB+CD-*"

# Infix to Postfix
print("Infix to Postfix:", infix_to_postfix(infix_expr))

# Infix to Prefix
print("Infix to Prefix:", infix_to_prefix(infix_expr))

# Prefix to Infix
print("Prefix to Infix:", prefix_to_infix(prefix_expr))

# Prefix to Postfix
print("Prefix to Postfix:", prefix_to_postfix(prefix_expr))

# Postfix to Prefix
print("Postfix to Prefix:", postfix_to_prefix(postfix_expr))

# Postfix to Infix
print("Postfix to Infix:", postfix_to_infix(postfix_expr))
