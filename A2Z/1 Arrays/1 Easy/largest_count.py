def largest_count(arr):
    # max_number = max(arr)
    # frequency = arr.count(max_number)
    
    max_num = 0
    for i in arr:
        if i > max_num:
            max_num = i
    
    return arr.count(max_num)

print(largest_count([1,2,3,4,4,4,4,5,5,6,6,6,6,8,9,9,9,9,9]))