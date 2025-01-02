# sort it such that the top of the stack has the greatest element


def sortedInsert(stack, element):
    # If the stack is empty or the top element is greater than the element
    # we want to insert, we can directly push the element
    if not stack or stack[-1] < element:
        stack.append(element)

    # Otherwise, pop the top element and recursively insert the element
    else:
        temp = stack.pop()
        sortedInsert(stack, element)
        stack.append(temp)


def sort_stack(s):
    if not s:
        return

    top = s.pop()
    sort_stack(s)
    sortedInsert(s, top)


s = [34, 3, 31, 98, 92, 23]
sort_stack(s)
print(s.pop())  # returns the largest element - 98
