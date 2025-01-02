# all steps similar to sort stack
# only difference is in insert_at_bottom function
# we directly append the new element to the stack
# without compraing with top element

def insert_at_bottom(stack, element):
    if not stack:
        stack.append(element)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, element)
        stack.append(temp)


def reverse_stack(stack):
    if not stack:
        return
    top_element = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, top_element)


stack = [1, 3, 5, 4, 2]
print("Original Stack:", stack)

reverse_stack(stack)
print("Reversed Stack:", stack)
