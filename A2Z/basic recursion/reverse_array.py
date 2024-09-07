def reverse_array(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse_array(arr, start+1, end-1)
    return arr

arr = [1, 2, 3, 4, 5]
print(reverse_array(arr, 0, len(arr)-1))

# using for loop
# def reverse_array(arr):
#     start = 0
#     end = len(arr) - 1
#     while start < end:
#         arr[start], arr[end] = arr[end], arr[start]
#         start += 1
#         end -= 1
#     return arr

